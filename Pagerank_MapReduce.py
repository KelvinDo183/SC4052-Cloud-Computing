from pyspark.sql import SparkSession
from pyspark.sql.functions import explode, col, lit, size, sum as _sum, array, collect_list


def initialize_spark_session():
    return SparkSession.builder.appName("PageRank").getOrCreate()


def create_links_df(spark, edges):
    links_df = spark.sparkContext.parallelize(edges).toDF(["src", "dst"])
    return links_df.groupBy("src").agg(collect_list("dst").alias("adj_list"))


def run_pagerank(spark, links_df, iterations=10):

    ranks_df = links_df.select("src").distinct(
    ).withColumn("rank", lit(1.0 / 4.0))

    for _ in range(iterations):
        # Calculate contributions by exploding the adjacency list
        contribs_df = links_df.join(ranks_df, "src") \
                              .select(explode("adj_list").alias("dst"), (col("rank") / size("adj_list")).alias("contrib"))

        # Sum contributions by destination node and apply the damping factor
        ranks_df = contribs_df.groupBy("dst").agg(
            _sum("contrib").alias("sum_contrib"))
        ranks_df = ranks_df.withColumn("rank", col(
            "sum_contrib") * 0.85 + 0.15 * (1.0 / 4.0))
        # Rename column for the next iteration
        ranks_df = ranks_df.select(col("dst").alias("src"), "rank")

        # Normalize ranks so that their sum equals 1
        total_rank = ranks_df.select(
            _sum("rank").alias("total")).collect()[0]["total"]
        ranks_df = ranks_df.withColumn("rank", col("rank") / total_rank)

    return ranks_df


if __name__ == "__main__":
    spark = initialize_spark_session()

    file_path = 'Graph/graph_lecture.txt'
    edges = []
    with open(file_path, 'r') as file:
        for line in file:
            # Adjust split() based on the file format
            source, target = map(int, line.strip().split())
            edges.append((source, target))

    links_df = create_links_df(spark, edges)

    final_ranks_df = run_pagerank(spark, links_df)

    final_ranks_df.show()
    spark.stop()
