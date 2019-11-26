# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s bgetem.hautschutz -t test_desinfektionsmittel.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src bgetem.hautschutz.testing.BGETEM_HAUTSCHUTZ_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot /src/bgetem/hautschutz/tests/robot/test_desinfektionsmittel.robot
#
# See the http://docs.plone.org for further details (search for robot
# framework).
#
# ============================================================================

*** Settings *****************************************************************

Resource  plone/app/robotframework/selenium.robot
Resource  plone/app/robotframework/keywords.robot

Library  Remote  ${PLONE_URL}/RobotRemote

Test Setup  Open test browser
Test Teardown  Close all browsers


*** Test Cases ***************************************************************

Scenario: As a site administrator I can add a Desinfektionsmittel
  Given a logged-in site administrator
    and an add Desinfektionsmittel form
   When I type 'My Desinfektionsmittel' into the title field
    and I submit the form
   Then a Desinfektionsmittel with the title 'My Desinfektionsmittel' has been created

Scenario: As a site administrator I can view a Desinfektionsmittel
  Given a logged-in site administrator
    and a Desinfektionsmittel 'My Desinfektionsmittel'
   When I go to the Desinfektionsmittel view
   Then I can see the Desinfektionsmittel title 'My Desinfektionsmittel'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add Desinfektionsmittel form
  Go To  ${PLONE_URL}/++add++Desinfektionsmittel

a Desinfektionsmittel 'My Desinfektionsmittel'
  Create content  type=Desinfektionsmittel  id=my-desinfektionsmittel  title=My Desinfektionsmittel

# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IBasic.title  ${title}

I submit the form
  Click Button  Save

I go to the Desinfektionsmittel view
  Go To  ${PLONE_URL}/my-desinfektionsmittel
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a Desinfektionsmittel with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the Desinfektionsmittel title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
