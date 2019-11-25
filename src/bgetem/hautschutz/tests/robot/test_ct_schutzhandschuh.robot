# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s bgetem.hautschutz -t test_schutzhandschuh.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src bgetem.hautschutz.testing.BGETEM_HAUTSCHUTZ_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot /src/bgetem/hautschutz/tests/robot/test_schutzhandschuh.robot
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

Scenario: As a site administrator I can add a Schutzhandschuh
  Given a logged-in site administrator
    and an add Schutzhandschuh form
   When I type 'My Schutzhandschuh' into the title field
    and I submit the form
   Then a Schutzhandschuh with the title 'My Schutzhandschuh' has been created

Scenario: As a site administrator I can view a Schutzhandschuh
  Given a logged-in site administrator
    and a Schutzhandschuh 'My Schutzhandschuh'
   When I go to the Schutzhandschuh view
   Then I can see the Schutzhandschuh title 'My Schutzhandschuh'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add Schutzhandschuh form
  Go To  ${PLONE_URL}/++add++Schutzhandschuh

a Schutzhandschuh 'My Schutzhandschuh'
  Create content  type=Schutzhandschuh  id=my-schutzhandschuh  title=My Schutzhandschuh

# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IBasic.title  ${title}

I submit the form
  Click Button  Save

I go to the Schutzhandschuh view
  Go To  ${PLONE_URL}/my-schutzhandschuh
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a Schutzhandschuh with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the Schutzhandschuh title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
