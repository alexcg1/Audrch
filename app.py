from jina import Flow
import pretty_errors
from docarray import DocumentArray

DATA_DIR = "./data/esc-50/audio/"


def load_data(data_dir=DATA_DIR, targets=[0], extension="wav"):
    final_docarray = DocumentArray()
    for target in targets:
        docs_source = f"{data_dir}/*-{str(target)}.{extension}"
        docs = DocumentArray.from_files(docs_source)
        final_docarray.extend(docs)

    return final_docarray


def main():
    docs = load_data()

    flow = Flow.load_config("flow.yml")
    with flow:
        index = flow.index(inputs=docs, show_progress=True, return_results=True)
        flow.protocol = "http"
        flow.cors = True
        flow.block()


if __name__ == "__main__":
    main()
