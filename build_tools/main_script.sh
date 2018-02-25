echo "#####################################################"
echo "#      Build start time : $(date +"%T, %F")      #"
echo "#####################################################"
export workspace=/var/lib/jenkins/workspace/Build_Automation
#export workspace=~/Git_Jenkins/Jenkins_CI_Setup
export toolpath=$workspace/build_tools
export sourcepath=source_code
export headerpath=headers
cd $workspace
python $toolpath/build.py $sourcepath $headerpath
make
echo $'\n'
echo "Final code output :"
#echo $'\n'
./finalmake
#echo $?
set exitstatus=$?
echo $'\n'
echo "#####################################################"
echo "#       Build end time : $(date +"%T, %F")       #"
echo "#####################################################"
echo "Performing the clean"
make clean
if [ "$exitstatus" == 0 ]
then 	
	echo Build Success!!
else
	echo Build Failed!!
fi
