from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.documents import Document

documents = [
    Document(
        page_content="""
        Virat Kohli is one of the greatest batsmen in cricket history and the highest run-scorer in IPL history.
        He has represented Royal Challengers Bengaluru throughout his IPL career.
        Kohli is known for his consistency, aggressive batting style, leadership, and ability to chase targets.
        He has scored thousands of IPL runs and remains the face of Royal Challengers Bengaluru.
        """,
        metadata={
            "player": "Virat Kohli",
            "team": "Royal Challengers Bengaluru",
            "role": "Batsman",
        },
    ),
    Document(
        page_content="""
        MS Dhoni is one of the most successful captains in IPL history.
        He captained Chennai Super Kings to multiple IPL championships.
        Dhoni is famous for his calm leadership, finishing ability, and wicketkeeping skills.
        He is regarded as one of the greatest finishers in cricket.
        """,
        metadata={
            "player": "MS Dhoni",
            "team": "Chennai Super Kings",
            "role": "Wicketkeeper-Batsman",
        },
    ),
    Document(
        page_content="""
        Rohit Sharma is a successful IPL captain and opening batsman.
        He led Mumbai Indians to multiple IPL titles.
        Rohit is known for elegant stroke play, match-winning innings, and leadership qualities.
        He is among the highest run scorers in IPL history.
        """,
        metadata={
            "player": "Rohit Sharma",
            "team": "Mumbai Indians",
            "role": "Batsman",
        },
    ),
    Document(
        page_content="""
        Jasprit Bumrah is one of the best fast bowlers in world cricket.
        He plays for Mumbai Indians in the IPL.
        Bumrah is famous for his yorkers, death-over bowling, and ability to take wickets under pressure.
        He has been a key contributor to Mumbai Indians' success.
        """,
        metadata={
            "player": "Jasprit Bumrah",
            "team": "Mumbai Indians",
            "role": "Bowler",
        },
    ),
    Document(
        page_content="""
        AB de Villiers was a legendary South African batsman who played for Royal Challengers Bengaluru.
        Nicknamed Mr. 360, he could play shots all around the ground.
        He formed one of the most successful batting partnerships in IPL history with Virat Kohli.
        His explosive batting entertained fans worldwide.
        """,
        metadata={
            "player": "AB de Villiers",
            "team": "Royal Challengers Bengaluru",
            "role": "Batsman",
        },
    ),
]
vectorstore = Chroma.from_documents(
    documents=documents, embedding=HuggingFaceEmbeddings()
)
retriever = vectorstore.as_retriever(search_kwargs={"k": 2})
results = retriever.invoke("Who is the best batsman in IPL history?")
print(results)
