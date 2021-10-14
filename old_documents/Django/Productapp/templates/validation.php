<html>
    <head></head>
    <body>
        <script>
            functoion validateForm(){
                let uname = document.forms['myform']['name'].value;
                let email = document.forms['myform']['email'].value;
                let password = document.forms['myform']['password'].value;
                #let uname = document.forms['myform']['n'].value;
                #let uname = document.forms['myform']['name'].value;
                let name_regex = /^[a-zA-Z]+$/;
                let name_val = uname.match(name_regex)

                if(name_val == null){
                    alert('Invalid username');
                    document.myform.name.focus();
                    return false;
                }
                else:
                    alert('Hi');a

            }
        </script>
    </body
</html>
