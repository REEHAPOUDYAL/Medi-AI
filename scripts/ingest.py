from mediai.ingestion.loader import load_pdf
documents = load_pdf(
    "data/raw/WHO.pdf",
    start_page=21,
    end_page=25
)
for document in documents:
    print(document["metadata"])
    print(document["text"][:500])
