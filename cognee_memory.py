import logging
import cognee
from cognee import SearchType

class CogneeMemory:
    def __init__(self):
        """
        Initializes the Cognee AI memory manager abstraction layer.
        Uses Cognee's internal flag management to avoid duplicate orchestration.
        """
        pass

    async def initialize(self):
        """
        Ensures any system configurations or default ontology setups are initialized.
        In modern versions of Cognee, this step typically runs implicitly during operations,
        but keeping an async hook allows for custom schema injections.
        """
        try:
            # Placeholder for custom dataset/topology pruning or schema inventory setup
            logging.info("Cognee memory engine ready.")
        except Exception as e:
            logging.error(f"Error initializing Cognee: {e}")
            raise e

    async def add_interview_record(
        self, 
        topic: str, 
        question: str, 
        answer: str, 
        score: int, 
        feedback: str, 
        mistakes: list
    ):
        """
        Ingests a completed interview question interaction string into the 
        Cognee Knowledge Graph space.
        """
        # Formulate a structured narrative format so Cognee can map out entities & semantic ties
        interaction_summary = (
            f"Interview Performance Record:\n"
            f"- Topic: {topic}\n"
            f"- Question Asked: {question}\n"
            f"- Candidate Answer: {answer}\n"
            f"- Score Given: {score}/10\n"
            f"- Performance Feedback: {feedback}\n"
            f"- Mistakes Made: {', '.join(mistakes) if mistakes else 'None'}\n"
        )
        
        try:
            # Step 1: Add raw transaction text metadata into Cognee processing queue
            await cognee.add(data=interaction_summary, dataset_name="interview_history")
            
            # Step 2: Fire execution graph pipeline processing (extracts nodes, builds vector attachments)
            await cognee.cognify()
            logging.info(f"Successfully cognified interview interaction on topic: {topic}")
        except Exception as e:
            logging.error(f"Failed to add data block to Cognee Graph structure: {e}")
            raise e

    async def get_context_for_next_question(self) -> str:
        """
        Queries Cognee via hybrid Graph-Vector retrieval to pull a rich summary of 
        what the candidate has been asked, how they performed, and recurring knowledge themes.
        """
        try:
            # Query the Knowledge Graph using an open semantic anchor
            search_results = await cognee.search(
                query_type=SearchType.GRAPH_COMPLETION,
                query_text="Summarize the candidate's previous answers, evaluated scores, and performance context."
            )
            
            if search_results:
                # Merge individual graph string context chunks gracefully
                return "\n".join([str(result) for result in search_results])
                
            return "No previous interview context found in Knowledge Graph."
            
        except Exception as e:
            logging.error(f"Failed to recall knowledge state from Cognee: {e}")
            return "Error retrieving contextual timeline from graph backend."