function Function(inputtxt)
{ 
var letters = /^[a-z A-Z]+$/;
if(inputtxt.value.match(letters))
{
alert('Thanks');
X.Z.focus();
return true;
}
else
{
alert('Error');
return false;
}
}