#!/bin/bash
Student="student1_LP1_1"
echo "Running grading script on OpenLab server."
echo ""
echo "$ObjectiveHere (1pt):" 
echo ""
echo "Expected result: $CommandsToLookFor."
echo ""
if grep $Student /var/log/tac.acct | grep -q -o "$CommandsToLookFor"; then  
   echo "✅Objective complete.✅"
   completion=$((completion + 1))
else
   echo "🚫Objective not complete.🚫"
fi 
echo ""
echo "Objective 2 - $ObjectiveHere (1pt):"
echo "" 
echo "Expected result: $CommandsToLookFor."
echo ""
if grep $Student /var/log/tac.acct | grep -q -o "$CommandsToLookFor"; then  
   echo "✅Objective complete.✅"
   completion=$((completion + 1))
else
   echo "🚫Objective not complete.🚫"
fi 
echo ""
echo "Objective 3 - $ObjectiveHere (1pt):"
echo "" 
echo "Expected result: $CommandsToLookFor."
echo ""
if grep $Student /var/log/tac.acct | grep -q -o "$CommandsToLookFor"; then  
   echo "✅Objective complete.✅"
   completion=$((completion + 1))
else
   echo "🚫Objective not complete.🚫"
fi 
echo ""
echo "Objective 4 - $ObjectiveHere (1pt):"
echo "" 
echo "Expected result: $CommandsToLookFor."
echo ""
if grep $Student /var/log/tac.acct | grep -q -o "$CommandsToLookFor"; then  
   echo "✅Objective complete.✅"
   completion=$((completion + 1))
else
   echo "🚫Objective not complete.🚫"
fi 
echo ""
echo "Objective 5 - $ObjectiveHere (1pt):"
echo "" 
echo "Expected result: $CommandsToLookFor."
echo ""
if grep $Student /var/log/tac.acct | grep -q -o "$CommandsToLookFor"; then  
   echo "✅Objective complete.✅"
   completion=$((completion + 1))
else
   echo "🚫Objective not complete.🚫"
fi 
echo ""
echo "Objective 6 - $ObjectiveHere (1pt):"
echo "" 
echo "Expected result: $CommandsToLookFor."
echo ""
if grep $Student /var/log/tac.acct | grep -q -o "$CommandsToLookFor"; then  
   echo "✅Objective complete.✅"
   completion=$((completion + 1))
else
   echo "🚫Objective not complete.🚫"
fi 
echo ""
echo "Objective 7 - $ObjectiveHere (1pt):"
echo "" 
echo "Expected result: $CommandsToLookFor."
echo ""
if grep $Student /var/log/tac.acct | grep -q -o "$CommandsToLookFor"; then  
   echo "✅Objective complete.✅"
   completion=$((completion + 1))
else
   echo "🚫Objective not complete.🚫"
fi 
echo ""
echo "Objective 8 - $ObjectiveHere (1pt):" 
echo ""
echo "Expected result: $CommandsToLookFor."
echo ""
if grep $Student /var/log/tac.acct | grep -q -o "$CommandsToLookFor"; then  
   echo "✅Objective complete.✅"
   completion=$((completion + 1))
else
   echo "🚫Objective not complete.🚫"
fi 
echo ""
echo "Objective 9 - $ObjectiveHere (1pt):"
echo "" 
echo "Expected result: $CommandsToLookFor."
echo ""
if grep $Student /var/log/tac.acct | grep -q -o "$CommandsToLookFor"; then  
   echo "✅Objective complete.✅"
   completion=$((completion + 1))
else
   echo "🚫Objective not complete.🚫"
fi 
echo ""
echo "Objective 10 - $ObjectiveHere (1pt):"
echo "" 
echo "Expected result: transport input ssh."
echo ""
if grep $Student /var/log/tac.acct | grep -q -o "$CommandsToLookFor"; then  
   echo "✅Objective complete.✅"
   completion=$((completion + 1))
else
   echo "🚫Objective not complete.🚫"
fi
echo "" 
echo "Lab completion is $completion/10 pts."
if [[ "$completion" -eq 10 ]]; then
   nohup ansible-playbook /etc/ansible/playbooks/openlab_reload.yml &> /dev/null &
else
   echo "Not complete."  
fi
