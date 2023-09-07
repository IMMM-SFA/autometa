
import streamlit as st
from datetime import datetime as dt
import random
import string

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

    # provide an code reference
    st.markdown(
        """
        ### Code Reference:
        Provide a code reference for your research.
        """
    )

    # entry box for authors, to put the code reference!
    code = st.text_input(
        label="**Code**", 
        placeholder=""
    )

 # provide an data input
    st.markdown(
        """
        ### Data references:
        Provide a Data for your research.
        """
    )

    st.markdown(
        """
        ## Data references:
        Reference for each minted data source for your input data.
        """
    )

    # entry box for authors, to put the input data!
    dataset = st.text_input(
        label="**input data set**", 
        placeholder="input dataset"
    )

    linkreference = st.text_input(
        label="**input link reference**", 
        placeholder="input link"
    )

    DOI = st.text_input(
        label="**input DOI**", 
        placeholder="input DOI"
    )

    st.markdown(
        """
        Reference for each minted data source for your output data.
        """
    )

     # entry box for authors, to put the output data!
    datasetOutput = st.text_input(
        label="**output data set**", 
        placeholder="output dataset"
    )

    linkreferenceOutput = st.text_input(
        label="**output link reference**", 
        placeholder="output link"
    )

    DOIOutput = st.text_input(
        label="**output DOI**", 
        placeholder="output DOI"
    )


    st.markdown(
        """
        ### Contributing modeling software
        What software did you use in your work?
        """
    )

    contributions = st.text_input(
        label="**contributions**", 
        placeholder="model, version, link, DOI"
    )

    st.markdown(
        """
        ### Reproduce my experiment
        Fill in detailed info here or link to other documentation 
        that is a thorough walkthrough of how to use what is in 
        this repository to reproduce your experiment        
        """
    )

    experiment = st.text_input(
        label="**experiment**", 
        placeholder="script name, description, how to run"
    )

    st.markdown(
        """
        ### Reproduce my figures
        Use the scripts found in the `figures` directory to
        reproduce the figures used in this publication.
        """
    )

    figures = st.text_input(
        label="**figures**", 
        placeholder="script name, description, how to run"
    )

    if 'count' not in st.session_state:
	    st.session_state.count = 0

    def add_new_row():
        st.text_input("Please input something",key=random.choice(string.ascii_uppercase)+str(random.randint(0,999999)))

    if st.button("Add new row"):
        st.session_state.count += 1
        add_new_row()
        if st.session_state.count>1:
            for i in range(st.session_state.count-1):
                add_new_row()


    # submit button for form
    submitted = st.form_submit_button("Generate Document")

    # generate the preview on click
    if submitted:

        modelsList = contributions.split(",")

        if(len(modelsList) > 3):
            model = modelsList[0]
            modelversion = modelsList[1]
            modelLink = modelsList[2]
            modelDOI = modelsList[3]
        else:
            model = ""
            modelversion = ""
            modelLink = ""
            modelDOI = ""

        expList = experiment.split(",")   
        if(len(expList) > 2):
            scriptName = expList[0]
            description = expList[1]
            run = expList[2]
        else:
            scriptName = ""
            description = ""
            run = ""

        figList = figures.split(",")   
        if(len(figList) > 2):
            figscriptName = figList[0]
            figdescription = figList[1]
            figrun = figList[2]
        else:
            figscriptName = ""
            figdescription = ""
            figrun = ""
        
        document = f"""
        # {repo_name}

        **{title}**

        {authors}

        ## Abstract
        {abstract}

        ## Journal reference
        {journal}

        ## Code reference
        {code}

        ## Data references

        ### Input data
        |       Dataset       |                                   Repository Link                                    |               DOI                |
        |:-------------------:|:------------------------------------------------------------------------------------:|:--------------------------------:|
        |{dataset} | {linkreference} | {DOI} |
        
        ### Output data
        |       Dataset       |                                   Repository Link                                    |               DOI                |
        |:-------------------:|:------------------------------------------------------------------------------------:|:--------------------------------:|
        |{datasetOutput} | {linkreferenceOutput} | {DOIOutput} |
        
        ### Contributing models
        | Model | Version | Repository Link | DOI |
        |-------|---------|-----------------|-----|
        | {model} | {modelversion} | {modelLink} | {modelDOI} |

        ### Reproduce my experiment
        | Script Name | Description | How to Run |
        | --- | --- | --- |
        | {scriptName} |  {description} | {run} |
        {extra}

        ### Reproduce my figures
        | Script Name | Description | How to Run |
        | --- | --- | --- |
        | {figscriptName} |  {figdescription} | {figrun} |


        """  
        
        st.markdown("### Document Preview:")
        st.success(document)

