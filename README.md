# FileUpdateAlgorithm

<h2>Project Description</h2>
An allow list of IP addresses is used at my company to limit access to content that is restricted.
 They are listed in the "allow_list.txt" file. IP addresses that should no longer have access to this content are listed on a separate delete list. To automatically update the "allow_list.txt" file and delete certain IP addresses that shouldn't have access, I developed an algorithm.
<br />



<h2>Open the file that contains the allow list</h2>

<p align="center">
I started by opening the "allow_list.txt" file for the algorithm's first step. I first gave the import_file variable this file name as a string:
<br/>
  
  
<img src="https://i.imgur.com/lq4velq.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
 
Then, I used a with statement to open the file: <br/>
  
  <img src="https://i.imgur.com/8QW53BF.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
  
  In my algorithm, the allow list file is opened in read mode using the.open() function and the with statement to read it. My access to the IP addresses kept in the allow list file will be made possible by accessing the file. By shutting the file when the with statement is finished, the with keyword will aid in resource management. The open() function contains two parameters in the code with import_file, "r" as the file: parameter. First, I specify the file to import, and then I specify what I want to do with that file in the second. The letter "r" here denotes my desire to read it. As I work inside the with statement, the code also uses the as keyword to assign a variable called file, which stores the results of the.open() function.<br/>
  
  
  <h2>Read the file contents</h2>

<p align="center">
In order to read the file contents, I used the .read() method to convert it into the string.
<br/>
  
  
<img src="https://i.imgur.com/bGyUFmz.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
 
I can use the.read() function in the with statement's body when utilizing an.open() method that has the argument "r" for "read." I can read the file by converting it to a string using the.read() method. The file variable mentioned in the with statement was subjected to the.read() method. Then I set the variable ip_addresses to contain the textual output of this procedure.
In short, this method converts the "allow_list.txt" file's contents into a string format so that I may utilize the string in my Python application to organize and retrieve data.
 <br/>
 
  
 <h2>Convert the string into a list</h2>

<p align="center">
In order to remove individual IP addresses from the allow list, I needed it to be in list format. Therefore, I next used the .split() method to convert the ip_addresses string into a list:
<br/>
  
  
<img src="https://i.imgur.com/az0IJy8.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
 
 You can use a string variable to append the.split() function to. It operates by turning a string's contents into a list. To make it simpler to delete IP addresses from the allow list, ip_addresses has been divided into a list. The.split() function divides text into list elements by default based on whitespace. In this algorithm, the data contained in the variable ip_addresses, which is a string of IP addresses, each separated by a whitespace, is converted into a list of IP addresses by the.split() function. I reassigned this list back to the ip_addresses variable to store it.  <br/>
  
  
   <h2>Iterate through the remove list</h2>

<p align="center">

A key part of my algorithm involves iterating through the IP addresses that are elements in the
remove_list. To do this, I incorporated a for loop:
<br/>
  
<img src="https://i.imgur.com/0QPF7bC.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
   
   <h2>Remove IP addresses that are on the remove list</h2>

<p align="center">

Any IP address in the allow list, ip_addresses, that is also in the remove_list must be removed according to the algorithm. I was able to include the.remove() method in the body of my for loop in the following fashion since all of the entries in remove_list are also in the ip_addresses list and the ip_addresses list does not contain duplicates:
<br/>
  
<img src="https://i.imgur.com/k8BWpQP.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
 
I applied.remove() to ip_addresses because the IP addresses in the remove_list need to be removed from the list of IP addresses. To ensure that each IP address in the remove_list was removed from ip_addresses, I passed in the loop variable element as an argument. <br/>
  
  
   <h2>Update the file with the revised list of IP addresses </h2>

<p align="center">

I had to update the allow list file with the updated list of IP addresses as the last step in my method. I have to first change the list back into a string in order to achieve that. For this, I employed the.join() method:
<br/>
  
<img src="https://i.imgur.com/UPGsjqp.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
 
The iterable's contents are all combined into a string using the.join() method. A string that contains characters that, when joined into a string, will divide the iterable's elements is given to the.join() method. In this approach, I created a string from the list of ip_addresses using the.join() method so that I could send it as an argument to the.write() method when writing to the "allow_list.txt" file. The separator was a single space (" ").

I then updated the file using a second with statement and the.write() method: <br/>
  
  <img src="https://i.imgur.com/v4ycHfd.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
  
  This time, I added a second argument of "w" to my with statement's use of the open() method. With this parameter, I'm trying to open a file so I can change its contents. I can use this argument "w" to invoke the.write() function in the with statement's main body. The .write() function replaces any existing file content and writes string data to the specified file.

In this instance, I wanted to add a string with the updated allow list to the "allow_list.txt" file.
 Any IP addresses that were deleted from the allow list will no longer have access to the restricted material. I added the.write() function to the file object file that I specified in the with statement in order to overwrite the file. I used the ip_addresses variable as a parameter to indicate that the data in this variable should be used in place of the contents of the file mentioned in the with statement. <br/>

  
<h2>Summary</h2>
I developed an algorithm that eliminates IP addresses from the "allow_list.txt" file of authorized IP addresses that are listed in a remove_list variable. Opening the file, transforming it to a string that could be read, and then turning that string into a list that was kept in the variable ip_addresses were all steps in this procedure. I then used the.remove() method to delete each IP address from the ip_addresses list as I iterated through the IP addresses in the remove_list. Then, in order to replace the IP address list in the "allow_list.txt" file with the updated list, I used the.join() technique to turn the IP addresses back into strings.
<br />
