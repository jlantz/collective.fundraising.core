*** Settings ***

Library  Selenium2Library  timeout=10  implicit_wait=0.5
Library  OperatingSystem

Resource  plone/app/robotframework/selenium.robot
Resource  plone/app/robotframework/variables.robot
Resource  plone/app/robotframework/keywords.robot

Suite Setup  Start browser
Suite Teardown  Close All Browsers

*** Test Cases ***

Fundraising Settings behavior fields show in add form
    Go to homepage
    Login as site owner

    Create dexterity type  Test Fundraising Settings
    Enable behavior  Fundraising Settings

    Go to homepage
    Open Add New Menu
    Click link  xpath=//a/span[contains(., "Test Fundraising Settings")]/..
    Wait until page contains  Add Test Fundraising Settings

    ${src}=    Selenium2Library.Get Source
    OperatingSystem.Create File    ${OUTPUT_DIR}/source.html    ${src}

    Input Text  form-widgets-IFundraisingSettings-cf_fs_org_name  Test Organization
    Input Text  form-widgets-IFundraisingSettings-cf_fs_ask_levels  5|5,10,25,50,100,250
    Input Text  form-widgets-IFundraisingSettings-cf_fs_ask_level  5
    Input Text  form-widgets-IFundraisingSettings-cf_fs_goal  100


*** Keywords ***

Start browser
    Open browser  ${PLONE_URL}

Create dexterity type
    [Arguments]  ${title}
    Go to  ${PLONE_URL}/@@dexterity-types
    Click Overlay Button  css=#add-type input
    Input Text  css=#formfield-form-widgets-title input  ${title}
    Click Button  Add
    Wait until page contains element  link=Behaviors

Enable behavior 
    [Arguments]  ${name}
    Click Behaviors in edit bar
    ${for}=  Get element attribute  xpath=//label[contains(., "${name}")]@for
    Select checkbox  id=${for}

    Click button  Save
    Page should contain  Behaviors successfully updated
    Checkbox should be selected  id=${for}
