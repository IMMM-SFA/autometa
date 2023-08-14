
import streamlit as st
from datetime import datetime as dt


def list_authors():
    for index, entry in enumerate(st.session_state.author_list, start=1):
        st.markdown(f"{index}.  {entry}")


# Force responsive layout for columns also on mobile
st.write(
    """<style>
    [data-testid="column"] {
        width: calc(50% - 1rem);
        flex: 1 1 calc(50% - 1rem);
        min-width: calc(50% - 1rem);
    }
    </style>""",
    unsafe_allow_html=True,
)

# page title
st.title("Build your meta-repository document")

# description under title
st.markdown(
    """
    A meta-repository creates a single point of access for someone to 
    find all of the components that were used to create a published work 
    for the purpose of reproducibility. This repository should contain 
    references to all minted data and software as well as house any ancillary 
    code used to transform the source data, create figures for your 
    publication, conduct the experiment, and / or execute the 
    contributing software.

    Automatically build your meta-repository README.md file using 
    content you provide!
    See our [meta-repository](https://github.com/IMMM-SFA/metarepo) GitHub resource for more info!
    """
)

# entry form for content sections
with st.form("content"):

    st.write("Inside the form")

    # guidance for meta-repository name
    st.markdown(
        """
        ### Naming your meta-repository:

        The following naming conventions should be used when naming your repository:
        - Single author: **lastname_year_journal**
        - Multi author: **lastname-etal_year_journal**
        - Multiple publications in the same journal: **lastname-etal_year-letter_journal** (e.g., human-etal_2020-b_nature) 
        """
    )

    # entry box for meta-repository name - make lower case
    repo_name = st.text_input(
        label="**Repository Name**", 
        placeholder="lastname-etal_year_journal"
    ).casefold()

    # guidance for publication title
    st.markdown(
        """
        ### Publication title:
        This is usually the title of your publication. 
        """
    )

    # entry box for publication title
    title = st.text_input(
        label="**Publication Title**", 
        placeholder="The title of my publication."
    )

    # provide a list of authors
    st.markdown(
        """
        ### Author list:
        Provide a list of authors. 
        """
    )

    # entry box for authors
    authors = st.text_input(
        label="**Author List**", 
        placeholder="Human Being, Pacific Northwest National Laboratory"
    )

    # provide an abstract
    st.markdown(
        """
        ### Abstract:
        Provide an abstract or summary of your research.
        """
    )

    # entry box for authors
    abstract = st.text_input(
        label="**Abstract**", 
        placeholder=""
    )

    # provide an Journal
    st.markdown(
        """
        ### Journal Entry:
        Provide a journal citation for your research.
        """
    )

    # entry box for authors
    journal = st.text_input(
        label="**Journal**", 
        placeholder=""
    )


    # submit button for form
    submitted = st.form_submit_button("Generate Document")

    # generate the preview on click
    if submitted:

        document = f"""
        # {repo_name}

        **{title}**

        {authors}

        ## Abstract
        {abstract}

        ## Journal reference
        {journal}
        """

        st.markdown("### Document Preview:")
        st.success(document)

