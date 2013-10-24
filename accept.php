<?php


echo "<p>Please be patient. Your code is being compiled. Think happy thoughts. :D</p>";

$lang = $_POST['language'];
$code = $_POST['code'];
$random = $_POST['randomness'];

$the_event = substr($random, 0, 2);

//echo $my_event;

$the_question = substr($random, 2, 2);

//echo $my_question;

$the_user = substr($random, 4);

//echo $the_user;
if(!is_dir("files/event_".$the_event))
	{
		if(!mkdir("files/event_".$the_event, 0777) )
		{
			echo"<p><p>Can't create directory.";			
		}
		else{
			if(!is_dir("files/event_".$the_event."/ques_".$the_question))
	        {
		        if(!mkdir("files/event_".$the_event."/ques_".$the_question, 0777) )
		        {
			        echo"<p><p>Can't create directory.";			
			    }	
			 }	
		}
	}
$file_name = "./files/event_".$the_event.'/ques_'.$the_question.'/'.$the_user.".".$lang;

if(file_exists($file_name)){
  unlink($file_name);
  }
exec("chmod $file_name 0777");
$file=fopen($file_name,"w+") or die("cant open file");

fwrite($file, $code);


$my_event = substr($random, 0, 2);

//echo $my_event;

$my_question = substr($random, 2, 2);

//echo $my_question;

$the_user = substr($random, 4);

//echo $the_user;


if($lang == 'c')
{
    $my_lang = 1;
}
else if($lang == 'cpp')
{
    $my_lang = 2;
}

else if($lang == 'py')
{
    $my_lang =3;
}
$args=$my_lang.$random;

exec("chmod compiler.py 0777"); 

$cmd ="python compiler.py ".$args;

$result = -1;
$result = exec($cmd);
echo "<p>$result</p>";
{
switch ($result)
    {
        case -1:
            echo "No change from compiler.py";
            break;
        case 1:
            echo "Correct answer";
            break;
        case 2:
            echo "Wrong answer. Please try again.";
            break;
        case 3:
            echo "Compilation error.";
            break;
        case 4:
            echo "Run time error.";
            break;
        default:
            echo "Default case error.";
            break;
            
            }
}
//else
//echo " Execution Unsuccessfull!!";

?>
