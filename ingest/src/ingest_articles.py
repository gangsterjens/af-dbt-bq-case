import pandas as pd
import json
from pathlib import Path


def get_articles():

    BASE_DIR = Path(__file__).resolve().parent.parent  # = dn-case/
    DATA_DIR = BASE_DIR / "Data"
    path = DATA_DIR / "lantern_articles.json"
    with open(path, 'r') as f:
        data = json.load(f)

    main = []
    lantern_ids = []
    authors = []
    categories_list = []
    tags_list = []
    for el in data:
        lantern_id = el.get('lantern_id')
        # Fjerne duplikater ved å legge id i liste. hvis i liste, drop loop
        if lantern_id in lantern_ids:
            continue
        ingestion_time=el.get('ingestiontime')
        #tekst = el['body_html']
        lead_text = el.get('lead_text')
        title = el.get('title')
        publication = el.get('publication')
        url = el.get('url')
        published_date = el.get('published_date')
        updated_date = el.get('updated_date')

        main.append({
                    'lantern_id': lantern_id,
                    'ingestion_time': ingestion_time,
                    'published_at': published_date,
                    'updated_date': updated_date,
                    #'body_html': tekst,  ### Orker ikke laste opp all teksten.. 
                    'lead_text': lead_text, 
                    'title': title,
                    'publication': publication})
        ## Legge de nesta objektene i egne tabeller, loope over og legge ved lantern-id for å koble tilbake senere

        # Tags
        tags = el.get('tags')
        if tags and len(tags) > 0:
            for tag in tags:
                tag_name = tag.get('tag_name')
                tag_el = tag.get('tag')
                tags_list.append({
                    'lantern_id': lantern_id,
                    'tag': tag_el,
                    'tag_name': tag_name
                    })

        # Authors:
        byline = el.get('byline')
        byline = byline.get('authors')
        if byline and len(byline) > 0:
            for by in byline:
                author = by.get('author')
                author_id = by.get('author_id')
                author_username = by.get('author_username')
                author_name = by.get('author_name')
                author_email = by.get('author_email')
                authors.append({
                    'lantern_id': lantern_id,
                    'author_id': author_id,
                    'author_username': author_username,
                    'author_name': author_name,
                    'author_email': author_email
                    })

        # Categories
        categories = el.get('categories')
        if categories and len(categories) > 0:
            for cat in categories:
                category = cat.get('category')
                category_name = cat.get('category_name')
                is_default = cat.get('is_default')
                categories_list.append({
                    'lantern_id': lantern_id,
                    'category': category,
                    'category_name': category_name,
                    'is_default': is_default})
        lantern_ids.append(lantern_id)


        df_main = pd.DataFrame(main)
        df_authors = pd.DataFrame(authors)
        df_categories = pd.DataFrame(categories_list)
        df_tags = pd.DataFrame(tags_list)

    return df_main, df_authors, df_categories, df_tags
