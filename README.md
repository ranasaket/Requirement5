# Requirement5
This code send mobile number from the API gateway to AWS LAMBDA function through GET request parameter(like 'mobile'='+91*****').
Then its sends OTP to that number(must be verified in SNS text message) and return that OTP to the API for further validation.

# steps 
<h5> step1: Create HTTP API gateway and a lambda function and configure API gateway to your lambda function.</h5>
<h5> step 2:copy paste the lambda handler function to your AWS lambda function.</h5>
<h5> step 3: send get request with mobile number associated with it.It will send the OTP as a response for further validation.</h5>


