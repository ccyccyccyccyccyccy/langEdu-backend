from langchain_community.document_loaders import PyPDFLoader

async def parse_pdf(path): #return 

    loader = PyPDFLoader(path)
    pages = []
    async for page in loader.alazy_load():
        pages.append(page)
    return pages

def get_hf_embeddings():
    from langchain_huggingface import HuggingFaceEmbeddings
    model_name = "sentence-transformers/all-MiniLM-L6-v2"
    model_kwargs = {'device': 'cpu'}
    encode_kwargs = {'normalize_embeddings': False}
    hf = HuggingFaceEmbeddings(
        model_name=model_name,
        model_kwargs=model_kwargs,
        encode_kwargs=encode_kwargs
    )
    return hf
