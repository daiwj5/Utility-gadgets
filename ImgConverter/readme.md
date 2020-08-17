# ImgConverter

Actually, it's a simple program only used for some specific situations.

For example, you were asked to hand in an online assignment, but you thought it was inconvenient to finish this assignment with computer and you decided to use handwriting. 


You took a picture of your assigment like this with all things done:
![test](https://github.com/daiwj5/Utility-gadgets/blob/master/ImgConverter/img/test.jpg)

Honestly speaking, we will get pictures like that using our phone most of the time, we found it was somewhat blur and unclear due to the exsisting shadow, and you wanted it to be more clear.

Here comes our ImgConverter, which can help you convert this image to Black-and-White pictures with customized conversion factor(0~255).

For example, set factor = 125, and we get pic below:
![new_test125](https://github.com/daiwj5/Utility-gadgets/blob/master/ImgConverter/img/new_test125.jpg)

Actually it's not a suitable factor for this case, hence we try to make it whiter.Set factor = 100, we get pic below:
![new_test100](https://github.com/daiwj5/Utility-gadgets/blob/master/ImgConverter/img/new_test100.jpg)

Now we get a more clear assigment picture and we can finally hand it to our teacher!

# Usage

* Installation of dependencies

Numpy and opencv-python should be installed.
```
pip install -r requirements.txt
```
And the version of python should be **python3**.

* Run

There are two way to convert your iamges.
First, run the script
```
> python3 ImgConverter.py
Input image name your want to convert, eg：1.jpg. Your image: 
```
And then input your image name, it can be relative path and absolute path. After that, please input ther factor:
```
Input your conversion factor (0~255, white->black), eg：125. Your factor:
```
And it will convert your image and save as a copy at the path of the script **ImgConverter.py**

The Second way to run the script is shown below:
```
usage: [python | python3] ImgConverter.py [option] [file 1] [file 2] ...
```
Options (only one)
```
-f [factor] : Set the factor, where factor show be a positive integer and the range of factor is [0, 255].
```

Example:
```
> python ImgConverter.py -f 101 test.jpg
Converting~ test.jpg
Save as new_test.jpg
```