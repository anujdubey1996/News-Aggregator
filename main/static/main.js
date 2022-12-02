function ValidateEmail() {

  var validRegex = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/;

  input = document.getElementById('email').value
  if(input == ''){ 
    alert('Email cannot be blank!');
  } else if (input.match(validRegex)) {

    return true;

  } else {

    alert("Invalid email address!");

    document.form1.text1.focus();

    return false;

  }

}

function ValidatePassword(){

  var validRegex = /^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$/;

  input = document.getElementById('password').value
  if(input == ''){ 
    
    alert('Password cannot be blank!');

  } else if (input.match(validRegex)) {

    document.form1.text1.focus();

    return true;

  } else {

    alert("Invalid Password!");

    document.form1.text1.focus();

    return false;

  }  
}

function validateLogin(){
  ValidateEmail();
  ValidatePassword();
}