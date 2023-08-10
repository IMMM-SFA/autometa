
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

if "author_list" not in st.session_state:
    st.session_state.author_list = []

if "rerun" not in st.session_state:
    st.session_state.rerun = False


# We want our variable assignments to persist while a user session is active
# so we use the following method to do so and give it an initial value
if "my_variable" not in st.session_state:
    st.session_state.my_variable = None 

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

    # entry box for number
    n_authors = st.number_input(
        label="**Number of authors**", 
        value=0
    )

    if st.session_state.rerun == True:
        st.session_state.rerun = False
        st.experimental_rerun()

    else:
        author = st.text_input(
            "Enter Author Name:", 
            value="", 
            placeholder= "I.M. Human"
        )

        affiliation = st.text_input(
            "Enter Author Affiliation:",
            value="",
            placeholder="Pacific Northwest National Laboratory, Richland, WA 99354"
        )

        if st.button('Add Author'):
            if author != "" and affiliation != "":
                st.session_state.author_list.append(f"{author}, {affiliation}")

    list_authors()

    # submit button for form
    submitted = st.form_submit_button("Submit")

    # generate the preview on click
    if submitted:

        document = f"""
        # {repo_name}

        **{title}**

        """

        st.markdown("### Document Preview:")
        st.success(document)
