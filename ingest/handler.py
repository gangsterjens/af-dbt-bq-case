import sys
import pandas as pd
from src.settings import settings as cfg
from src.bq_client import BQClient

# Ingest-filer
from src import ingest_gzip as ig
from src import ingest_articles as ia
from src import ingest_entities as ie
from src import ingest_keywords as ikw
from src import ingest_teaser_positions as itp


def main():
    bq = BQClient(
        app_json=cfg.GOOGLE_APPLICATION_CREDENTIALS,
        bq_project=cfg.BQ_PROJECT,
        bq_dataset=cfg.BQ_DATASET
    )

    # CLI Argument for å route jobber.. kan også være alle
    if len(sys.argv) < 2:
        print("❌ Please provide an argument: articles | entities | keywords | teaser | gzip | all")
        sys.exit(1)

    arg = sys.argv[1].lower()

    # GZIP ingestion
    if arg in ["gzip", "all"]:
        print("🧩 Ingesting gzip file ...")
        path = "Data/content_segments_stats_bq-results-20250828-092542.gzip"
        df_segments = ig.load_file_from_gzip(path)
        bq.upload_df(df_segments, "segment_stats")

    # Articles ingestion
    if arg in ["articles", "all"]:
        print("📰 Ingesting articles ...")
        df_main, df_authors, df_categories, df_tags = ia.get_articles()
        bq.upload_df(df_main, "artikler_hoved")
        bq.upload_df(df_authors, "artikler_byline")
        bq.upload_df(df_categories, "artikler_kategorier")
        bq.upload_df(df_tags, "artikler_tags")

    # Entities ingestion
    if arg in ["entities", "all"]:
        print("🔠 Ingesting entities ...")
        df_ent = ie.get_entities()
        bq.upload_df(df_ent, "entities")

    # Keywords ingestion
    if arg in ["keywords", "all"]:
        print("🏷️ Ingesting keywords ...")
        df_kw = ikw.get_keywords()
        bq.upload_df(df_kw, "keywords")

    # Teaser positions ingestion
    if arg in ["teaser", "all"]:
        print("📍 Ingesting teaser positions ...")
        df_t = itp.get_tp()
        bq.upload_df(df_t, "teaser_positions")

    print("✅ Done!")


if __name__ == "__main__":
    main()
