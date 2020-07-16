from typing import Optional
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = None


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}


def generate_html_response():
    html_content = """
<!DOCTYPE html>
<html>
<title>CV</title>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
<link rel='stylesheet' href='https://fonts.googleapis.com/css?family=Roboto'>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
<style>
    html,
    body,
    h1,
    h2,
    h3,
    h4,
    h5,
    h6 {
        font-family: Í"Roboto", sans-serif
    }
    
    .linkedin {
        position: relative;
        -webkit-animation: mymove 3s infinite;
        animation: mymove 3s infinite;
    }
    
    @-webkit-keyframes mymove {
        from {
            left: -40px;
        }
        to {
            left: 40px;
        }
    }
    
    @keyframes mymove {
        from {
            left: -40px;
        }
        to {
            left: 40px;
        }
    }
    
    .social {
        animation: bounce 5s alternate infinite ease-in;
    }
    
    @media screen and (min-width:701px) {
        @keyframes bounce {
            0% {
                transform: translateX(75%);
            }
            100% {
                transform: translateX(-75%);
            }
        }
        .social {
            color: white;
            display: inline-block;
        }
    }
    
    @media screen and (max-width:700px) {
        @keyframes bounce {
            0% {
                transform: translateY(+50%);
            }
            100% {
                transform: translateY(0);
            }
        }
        .social {
            color: white;
            display: block;
            /* needed to trigger update */
        }
    }
    /*Animacion avatar azul*/
    
    @-webkit-keyframes walk {
        from {
            background-position: 0px;
        }
        to {
            background-position: -1472px;
        }
        /* <-- width of spritesheet*/
    }
    
    @-moz-keyframes walk {
        from {
            background-position: 0px;
        }
        to {
            background-position: -1472px;
        }
    }
    
    @-o-keyframes walk {
        from {
            background-position: 0px;
        }
        to {
            background-position: -1472px;
        }
    }
    
    @keyframes walk {
        from {
            background-position: 0px;
        }
        to {
            background-position: -1472px;
        }
    }
    
    .capguy {
        width: 184px;
        height: 325px;
        background-image: url("http://www.achoweb.es/webs/imagenes/walk.png'");
        margin: 0 auto;
        -webkit-animation: walk 1s steps(8) infinite;
        -moz-animation: walk 1s steps(8) infinite;
        -o-animation: walk 1s steps(8) infinite;
        animation: walk 1s steps(8) infinite;
    }
</style>

<body class="w3-light-grey">
    <!-- Page Container -->
    <div class="w3-content w3-margin-top" style="max-width:1400px;">
        <!-- The Grid -->
        <div class="w3-row-padding">
            <!-- Left Column -->
            <div class="w3-third">
                <div class="w3-white w3-text-grey w3-card-4">
                    <div class="w3-display-container">
                        <!--<img src="http://www.achoweb.es/webs/imagenes/hack.jpg" style="width:100%" alt="Avatar">-->
                        <div class="capguy"></div>
                        <div class="w3-display-bottomleft w3-container w3-text-black">
                            <h2 style="color:black">Carlos</h2>
                        </div>
                    </div>
                    </br>
                    <div class="w3-container">
                        <p><i class="fa fa-briefcase fa-fw w3-margin-right w3-large w3-text-indigo"></i>Full Stack Developer</p>
                        <p><i class="fa fa-heart fa-fw w3-margin-right w3-large w3-text-indigo"></i>London (UK)</p>
                        <p><i class="fa fa-envelope fa-fw w3-margin-right w3-large w3-text-indigo"></i>carlos@achoweb.es</p>
                        <p><i class="fa fa-github fa-fw w3-margin-right w3-large w3-text-indigo"></i><a href="https://github.com/C0o1N0g1O" target="_blank" rel=”noopener noreferrer“ style="text-decoration:none">GitHub</a></p>
                        <hr>
                        <p class="w3-large"><b><i class="fa fa-desktop fa-fw w3-margin-right w3-text-indigo"></i>Programming Languages</b></p>
                        <p>Java</p>
                        <div class="w3-light-grey w3-round-xlarge w3-small">
                            <div class="w3-container w3-center w3-round-xlarge w3-indigo" style="width:90%">90%</div>
                        </div>
                        <p>Javascript (ECMAScript 6)</p>
                        <div class="w3-light-grey w3-round-xlarge w3-small">
                            <div class="w3-container w3-center w3-round-xlarge w3-indigo" style="width:90%">
                                <div class="w3-center w3-text-white">90%</div>
                            </div>
                        </div>
                        <p>PHP</p>
                        <div class="w3-light-grey w3-round-xlarge w3-small">
                            <div class="w3-container w3-center w3-round-xlarge w3-indigo" style="width:90%">90%</div>
                        </div>
                        <p>Dart</p>
                        <div class="w3-light-grey w3-round-xlarge w3-small">
                            <div class="w3-container w3-center w3-round-xlarge w3-indigo" style="width:90%">90%</div>
                        </div>
                        <p>Python</p>
                        <div class="w3-light-grey w3-round-xlarge w3-small">
                            <div class="w3-container w3-center w3-round-xlarge w3-indigo" style="width:80%">80%</div>
                        </div>
                        <p>Go (Google)</p>
                        <div class="w3-light-grey w3-round-xlarge w3-small">
                            <div class="w3-container w3-center w3-round-xlarge w3-indigo" style="width:80%">80%</div>
                        </div>
                        <p>C C++</p>
                        <div class="w3-light-grey w3-round-xlarge w3-small">
                            <div class="w3-container w3-center w3-round-xlarge w3-indigo" style="width:80%">80%</div>
                        </div>
                        <p>R</p>
                        <div class="w3-light-grey w3-round-xlarge w3-small">
                            <div class="w3-container w3-center w3-round-xlarge w3-indigo" style="width:50%">Learning</div>
                        </div>
                        <p>Solidity</p>
                        <div class="w3-light-grey w3-round-xlarge w3-small">
                            <div class="w3-container w3-center w3-round-xlarge w3-indigo" style="width:50%">Learning</div>
                        </div>
                        </br>
                        <p class="w3-large"><b><i class="fa fa-connectdevelop fa-fw w3-margin-right w3-text-indigo"></i>Markup Language,
                        Cascading Style Sheets, and Information</b></p>
                        <div class="w3-light-grey w3-round-xlarge w3-small">
                            <div class="w3-container w3-center w3-round-xlarge w3-indigo" style="width:100%"></div>
                        </div>
                        <p>HTML5 | CSS3 </p>
                        <div class="w3-light-grey w3-round-xlarge w3-small">
                            <div class="w3-container w3-center w3-round-xlarge w3-indigo" style="width:90%">90%</div>
                        </div>
                        <p>XML</p>
                        <div class="w3-light-grey w3-round-xlarge w3-small">
                            <div class="w3-container w3-center w3-round-xlarge w3-indigo" style="width:90%">90%</div>
                        </div>
                        </br>
                        <p class="w3-large"><b><i class="fa fa-connectdevelop fa-fw w3-margin-right w3-text-indigo"></i>FrameWorks | Libraries</b></p>
                        <div class="w3-light-grey w3-round-xlarge w3-small">
                            <div class="w3-container w3-center w3-round-xlarge w3-indigo" style="width:100%"></div>
                        </div>
                        <p>FlexBox</p>
                        <div class="w3-light-grey w3-round-xlarge w3-small">
                            <div class="w3-container w3-center w3-round-xlarge w3-indigo" style="width:90%">90%</div>
                        </div>
                        <p>BootsTrap</p>
                        <div class="w3-light-grey w3-round-xlarge w3-small">
                            <div class="w3-container w3-center w3-round-xlarge w3-indigo" style="width:90%">90%</div>
                        </div>
                        <p>jQuery</p>
                        <div class="w3-light-grey w3-round-xlarge w3-small">
                            <div class="w3-container w3-center w3-round-xlarge w3-indigo" style="width:90%">90%</div>
                        </div>
                        <p>Node.js</p>
                        <div class="w3-light-grey w3-round-xlarge w3-small">
                            <div class="w3-container w3-center w3-round-xlarge w3-indigo" style="width:90%">90%</div>
                        </div>
                        <p>React (Facebook)</p>
                        <div class="w3-light-grey w3-round-xlarge w3-small">
                            <div class="w3-container w3-center w3-round-xlarge w3-indigo" style="width:80%">80%</div>
                        </div>
                        <p>Angular (Google)</p>
                        <div class="w3-light-grey w3-round-xlarge w3-small">
                            <div class="w3-container w3-center w3-round-xlarge w3-indigo" style="width:80%">80%</div>
                        </div>
                        </br>
                        <p class="w3-large"><b><i class="fa fa-connectdevelop fa-fw w3-margin-right w3-text-indigo"></i>Databases</b></p>
                        <div class="w3-light-grey w3-round-xlarge w3-small">
                            <div class="w3-container w3-center w3-round-xlarge w3-indigo" style="width:100%"></div>
                        </div>
                        <p>SQL</p>
                        <div class="w3-light-grey w3-round-xlarge w3-small">
                            <div class="w3-container w3-center w3-round-xlarge w3-indigo" style="width:90%">90%</div>
                        </div>
                        <p>PL/SQL (Oracle)</p>
                        <div class="w3-light-grey w3-round-xlarge w3-small">
                            <div class="w3-container w3-center w3-round-xlarge w3-indigo" style="width:90%">90%</div>
                        </div>
                        <p>MySQL</p>
                        <div class="w3-light-grey w3-round-xlarge w3-small">
                            <div class="w3-container w3-center w3-round-xlarge w3-indigo" style="width:90%">90%</div>
                        </div>
                        <p>PostgreSQL</p>
                        <div class="w3-light-grey w3-round-xlarge w3-small">
                            <div class="w3-container w3-center w3-round-xlarge w3-indigo" style="width:90%">90%</div>
                        </div>
                        <p>MongoDB</p>
                        <div class="w3-light-grey w3-round-xlarge w3-small">
                            <div class="w3-container w3-center w3-round-xlarge w3-indigo" style="width:90%">90%</div>
                        </div>
                        <p>Realm</p>
                        <div class="w3-light-grey w3-round-xlarge w3-small">
                            <div class="w3-container w3-center w3-round-xlarge w3-indigo" style="width:90%">90%</div>
                        </div>
                        </br>
                        <p class="w3-large"><b><i class="fa fa-connectdevelop fa-fw w3-margin-right w3-text-indigo"></i>Systems</b></p>
                        <div class="w3-light-grey w3-round-xlarge w3-small">
                            <div class="w3-container w3-center w3-round-xlarge w3-indigo" style="width:100%"></div>
                        </div>
                        <p>Linux</p>
                        <div class="w3-light-grey w3-round-xlarge w3-small">
                            <div class="w3-container w3-center w3-round-xlarge w3-indigo" style="width:90%">90%</div>
                        </div>
                        <p>Apple</p>
                        <div class="w3-light-grey w3-round-xlarge w3-small">
                            <div class="w3-container w3-center w3-round-xlarge w3-indigo" style="width:90%">90%</div>
                        </div>
                        <p>Windows Server</p>
                        <div class="w3-light-grey w3-round-xlarge w3-small">
                            <div class="w3-container w3-center w3-round-xlarge w3-indigo" style="width:90%">90%</div>
                        </div>
                        </br>
                        <p class="w3-large"><b><i class="fa fa-connectdevelop fa-fw w3-margin-right w3-text-indigo"></i>Mobile</b></p>
                        <div class="w3-light-grey w3-round-xlarge w3-small">
                            <div class="w3-container w3-center w3-round-xlarge w3-indigo" style="width:100%"></div>
                        </div>
                        <p>Flutter</p>
                        <div class="w3-light-grey w3-round-xlarge w3-small">
                            <div class="w3-container w3-center w3-round-xlarge w3-indigo" style="width:80%">80%</div>
                        </div>
                        <p>Android</p>
                        <div class="w3-light-grey w3-round-xlarge w3-small">
                            <div class="w3-container w3-center w3-round-xlarge w3-indigo" style="width:80%">80%</div>
                        </div>
                        <p>Swift</p>
                        <div class="w3-light-grey w3-round-xlarge w3-small">
                            <div class="w3-container w3-center w3-round-xlarge w3-indigo" style="width:25%">Learning</div>
                        </div>
                        </br>
                        <p class="w3-large"><b><i class="fa fa-connectdevelop fa-fw w3-margin-right w3-text-indigo"></i>Shell Scripting</b></p>
                        <div class="w3-light-grey w3-round-xlarge w3-small">
                            <div class="w3-container w3-center w3-round-xlarge w3-indigo" style="width:100%"></div>
                        </div>
                        <p>Bash</p>
                        <div class="w3-light-grey w3-round-xlarge w3-small">
                            <div class="w3-container w3-center w3-round-xlarge w3-indigo" style="width:90%">90%</div>
                        </div>
                        <p>PowerShell</p>
                        <div class="w3-light-grey w3-round-xlarge w3-small">
                            <div class="w3-container w3-center w3-round-xlarge w3-indigo" style="width:90%">90%</div>
                        </div>
                        <p>Ansible</p>
                        <div class="w3-light-grey w3-round-xlarge w3-small">
                            <div class="w3-container w3-center w3-round-xlarge w3-indigo" style="width:80%">70%</div>
                        </div>
                        </br>
                        <p class="w3-large"><b><i class="fa fa-connectdevelop fa-fw w3-margin-right w3-text-indigo"></i>Virtualization Software</b></p>
                        <div class="w3-light-grey w3-round-xlarge w3-small">
                            <div class="w3-container w3-center w3-round-xlarge w3-indigo" style="width:100%"></div>
                        </div>
                        <p>VMWare</p>
                        <div class="w3-light-grey w3-round-xlarge w3-small">
                            <div class="w3-container w3-center w3-round-xlarge w3-indigo" style="width:90%">90%</div>
                        </div>
                        <p>VirtualBox</p>
                        <div class="w3-light-grey w3-round-xlarge w3-small">
                            <div class="w3-container w3-center w3-round-xlarge w3-indigo" style="width:90%">90%</div>
                        </div>
                        <p>Docker</p>
                        <div class="w3-light-grey w3-round-xlarge w3-small">
                            <div class="w3-container w3-center w3-round-xlarge w3-indigo" style="width:80%">80%</div>
                        </div>
                        <p>Vagrant</p>
                        <div class="w3-light-grey w3-round-xlarge w3-small">
                            <div class="w3-container w3-center w3-round-xlarge w3-indigo" style="width:80%">80%</div>
                        </div>
                        </br>
                        <p class="w3-large"><b><i class="fa fa-connectdevelop fa-fw w3-margin-right w3-text-indigo"></i>Cloud</b></p>
                        <div class="w3-light-grey w3-round-xlarge w3-small">
                            <div class="w3-container w3-center w3-round-xlarge w3-indigo" style="width:100%"></div>
                        </div>
                        <p>Firebase</p>
                        <div class="w3-light-grey w3-round-xlarge w3-small">
                            <div class="w3-container w3-center w3-round-xlarge w3-indigo" style="width:90%">90%</div>
                        </div>
                        <p>Google Cloud</p>
                        <div class="w3-light-grey w3-round-xlarge w3-small">
                            <div class="w3-container w3-center w3-round-xlarge w3-indigo" style="width:90%">90%</div>
                        </div>
                        <p>Cloud functions</p>
                        <div class="w3-light-grey w3-round-xlarge w3-small">
                            <div class="w3-container w3-center w3-round-xlarge w3-indigo" style="width:80%">80%</div>
                        </div>
                        <p>AWS</p>
                        <div class="w3-light-grey w3-round-xlarge w3-small">
                            <div class="w3-container w3-center w3-round-xlarge w3-indigo" style="width:80%">80%</div>
                        </div>
                        <p>Lambdas functions</p>
                        <div class="w3-light-grey w3-round-xlarge w3-small">
                            <div class="w3-container w3-center w3-round-xlarge w3-indigo" style="width:90%">90%</div>
                        </div>
                        </br>
                        <p class="w3-large"><b><i class="fa fa-connectdevelop fa-fw w3-margin-right w3-text-indigo"></i>API's</b></p>
                        <div class="w3-light-grey w3-round-xlarge w3-small">
                            <div class="w3-container w3-center w3-round-xlarge w3-indigo" style="width:100%"></div>
                        </div>
                        <p>REST</p>
                        <div class="w3-light-grey w3-round-xlarge w3-small">
                            <div class="w3-container w3-center w3-round-xlarge w3-indigo" style="width:90%">90%</div>
                        </div>
                        <p>GraphQL</p>
                        <div class="w3-light-grey w3-round-xlarge w3-small">
                            <div class="w3-container w3-center w3-round-xlarge w3-indigo" style="width:90%">90%</div>
                        </div>
                        </br>
                        <p class="w3-large"><b><i class="fa fa-connectdevelop fa-fw w3-margin-right w3-text-indigo"></i>NetWork CISCO</b></p>
                        <div class="w3-light-grey w3-round-xlarge w3-small">
                            <div class="w3-container w3-center w3-round-xlarge w3-indigo" style="width:100%"></div>
                        </div>
                        <p>Routing and Switching</p>
                        <div class="w3-light-grey w3-round-xlarge w3-small">
                            <div class="w3-container w3-center w3-round-xlarge w3-indigo" style="width:90%">90%</div>
                        </div>
                        <p>CCNA</p>
                        <div class="w3-light-grey w3-round-xlarge w3-small">
                            <div class="w3-container w3-center w3-round-xlarge w3-indigo" style="width:90%">Preparing</div>
                        </div>
                        </br>
                        <p class="w3-large w3-text-theme"><b><i class="fa fa-globe fa-fw w3-margin-right w3-text-indigo"></i>Languages</b></p>
                        <p>Spanish</p>
                        <div class="w3-light-grey w3-round-xlarge">
                            <div class="w3-round-xlarge w3-indigo" style="height:24px;width:100%"></div>
                        </div>
                        <p>English</p>
                        <div class="w3-light-grey w3-round-xlarge">
                            <div class="w3-round-xlarge w3-indigo" style="height:24px;width:80%"></div>
                        </div><br></div>
                </div><br>
                <!-- End Left Column -->
            </div>
            <!-- Right Column -->
            <div class="w3-twothird">
                <div class="w3-container w3-card w3-white w3-margin-bottom">
                    <h2 class="w3-text-grey w3-padding-16"><i class="fa fa-user-circle fa-fw w3-margin-right w3-xxlarge w3-text-indigo"></i>About me</h2>
                    <div class="w3-container">
                        <h5 class="w3-opacity"><b>Full Stack Developer </b></h5>
                        <h6 class="w3-text-indigo"><i class="fa fa-calendar fa-fw w3-margin-right"></i>2014 - <span class="w3-tag w3-indigo w3-round">Current</span></h6>
                        <p style="text-align: justify">
                            <p style="text-align:justify">Carlos is a Full Stack Developer familiar with the syntax of Programming languages such { ‘Java, PHP, Javascript, C, C++, Python, Golang, TypeScript'} | Frameworks or Libraries {‘Angular, NodeJS, ReactJS, Django’ } | Databases
                                { ‘MySQL, SQL, PL/SQL, SQL Server, PostgreSQL, MongoDB’ } | Control Version { ‘ Subversion, Git, Github’ } . </p>
                            <hr>
                    </div>
                    <div class="w3-container">
                        <h5 class="w3-opacity"><b>Team Worker </b></h5>
                        <h6 class="w3-text-indigo"><i class="fa fa-calendar fa-fw w3-margin-right"></i><span class="w3-tag w3-indigo w3-round">Current</span></h6>
                        <p style="text-align:justify">Interest and ability to learn other coding languages as needed. Comfortable working in a fast-paced technical enviroment and with cutting-edge technologies. A fast learner with the ability to adapt to new team enviroments and priorities
                            quicky. A phenomenal teammate and a passionate/energetic programmer.</p>
                    </div>
                </div>
                <div class="w3-container w3-card w3-white w3-margin-bottom">
                    <h2 class="w3-text-grey w3-padding-16"><i class="fa fa-suitcase fa-fw w3-margin-right w3-xxlarge w3-text-indigo"></i>Work Experience</h2>
                    <div class="w3-container">
                        <h5 class="w3-opacity"><b>Junior Full Stack Developer(Internship) at Everis (London) </b></h5>
                        <h6 class="w3-text-indigo"><i class="fa fa-calendar fa-fw w3-margin-right"></i>February 2020- June 2020</h6>
                        <p style="text-align: justify">
                            <p style="text-align:justify">* Flutter, Dart, JavaScript, TypeScript, NodeJS, MongoDB, GraphQL, Firebase, AWS </p>
                            <hr>
                    </div>
                    <div class="w3-container">
                        <h5 class="w3-opacity"><b>Graduate/Junior Oracle Developer (Internship) at Capgemini (Murcia) </b></h5>
                        <h6 class="w3-text-indigo"><i class="fa fa-calendar fa-fw w3-margin-right"></i>April 2019 - June 2019</h6>
                        <p style="text-align: justify">
                            <p style="text-align:justify">* Java 8 * SQL * PL/SQL </p>
                            <hr>
                    </div>
                    <div class="w3-container">
                        <h5 class="w3-opacity"><b>Project Achoweb </b></h5>
                        <h6 class="w3-text-indigo"><i class="fa fa-calendar fa-fw w3-margin-right"></i>2004 - <span class="w3-tag w3-indigo w3-round">Current</span></h6>
                        <p style="text-align: justify">
                            <p style="text-align:justify">Achoweb is my – portfolio - from which I program, design and develop from scratch or with the most popular mobile websites and applications from CMS, with emphasis on details, user interface animations, user interaction, API
                                and innovative technologies. </p>
                            <hr>
                    </div>
                    <div class="w3-container">
                        <h5 class="w3-opacity"><b>Project SW ™</b></h5>
                        <h6 class="w3-text-indigo"><i class="fa fa-calendar fa-fw w3-margin-right"></i>2014 - <span class="w3-tag w3-indigo w3-round">Current</span></h6>
                        <p style="text-align: justify">
                            <p style="text-align:justify">SW ™ is a startup - hobby - for technology lovers. It is currently the reference platform for the construction, configuration and equalization of Subwoofers (DIY), Speakers and Audio-Video equipment. </p>
                            <hr>
                    </div>
                    <div class="w3-container">
                        <h5 class="w3-opacity"><b>Gap Year London</b></h5>
                        <h6 class="w3-text-indigo"><i class="fa fa-calendar fa-fw w3-margin-right"></i>2013 - 2014 </h6>
                        <p style="text-align: justify">
                            <p style="text-align:justify">Carlos lived a gap year in London, traveling, living with people from all over the world, learning English and living a unique experience. I have a national insurance number. </p>
                            <hr>
                    </div>
                    <div class="w3-container">
                        <h5 class="w3-opacity"><b>Freelance Web Designer</b></h5>
                        <h6 class="w3-text-indigo"><i class="fa fa-calendar fa-fw w3-margin-right"></i>2007 - 2013 </h6>
                        <p style="text-align: justify">
                            <p style="text-align:justify">Design Websites from CMS with WordPress, PrestaShop, phpBB, Dolibarr, Moodle and cPanel. </p>
                            <hr>
                    </div>
                </div>
                <div class="w3-container w3-card w3-white">
                    <h2 class="w3-text-grey w3-padding-16"><i class="fa fa-university fa-fw w3-margin-right w3-xxlarge w3-text-indigo"></i>Education</h2>
                    <div class="w3-container">
                        <h5 class="w3-opacity"><b>Associate Degree (Bac+2), Computer Network Systems Management</b></h5>
                        <h6 class="w3-text-indigo"><i class="fa fa-calendar fa-fw w3-margin-right"></i>2019 - 2020</h6>
                        <p style="text-align:justify">
                            <ul>
                                <li>Programming with Java, HTML, XHTML, CSS and other related programming language</li>
                                <li>Knowledge of relational databases and SQL </li>
                                <li>Configuring, administrating and maintaining computer systems (Mac OS, Windows Server, Linux), guaranteeing system functionality, integrity of resources and services, with the required quality and complying with the current
                                    legislation.
                                </li>
                                <li>Safety and High Availability</li>
                                <li>Network Planning and Management (CISCO CCNA)</li>
                            </ul>
                        </p>
                        <p style="text-align:justify">Subjects: Operating Systems Implementation, Network Planning and Management, Hardware Fundamentals, Databases, Markup Language and Information Management Systems, Operating Systems Management, Network Services and Internet, Web
                            Applications Implementation, Database Management, Systems Administration, Safety and High Availability.</p>
                        <p>Associate Degree (Bac+2) is two years full-time.</p>
                    </div>
                    <div class="w3-container">
                        <h5 class="w3-opacity"><b>Associate Degree (Bac+2), Multi-platform Applications Development</b></h5>
                        <h6 class="w3-text-indigo"><i class="fa fa-calendar fa-fw w3-margin-right"></i>2018 - 2019</h6>
                        <p style="text-align:justify">
                            <ul>
                                <li>Programming with Java, C, C++, Python, Go and other related programming language</li>
                                <li>Proven Movil Design experience</li>
                                <li>Knowledge of Algorithms</li>
                                <li>Concurrency experience</li>
                                <li>Proven Data structures experience</li>
                                <li>Knowledge of relational databases and SQL</li>
                            </ul>
                        </p>
                        <p style="text-align:justify">Subjects: Computer Systems, Databases, Programming, Markup Language and Information Management Systems, Development Environments, Data Access, Interface Development, Multimedia Programming and Mobile Devices, Services and Processes
                            Programming, Business Management Systems. Technical knowledge of mobile application development (either Android or iOS).</p>
                        <p>Associate Degree (Bac+2) is two years full-time.</p>
                        <hr>
                    </div>
                    <div class="w3-container">
                        <h5 class="w3-opacity"><b>Associate Degree (Bac+2), Development of Web Applications</b></h5>
                        <h6 class="w3-text-indigo"><i class="fa fa-calendar fa-fw w3-margin-right"></i>2016 - 2018</h6>
                        <p style="text-align:justify">
                            <ul>
                                <li>Programming with Java, PHP, JavasCript, jQuery, HTML, XHTML, CSS and other related programming language</li>
                                <li>Proven Web Design experience</li>
                                <li>Knowledge of Algorithms</li>
                                <li>Proven Data structures experience</li>
                                <li>Knowledge of relational databases and SQL </li>
                            </ul>
                        </p>
                        <p style="text-align:justify">Subjects: Computer Systems, Databases, Programming, Markup Language and Information Management Systems, Development Environments, Web Development in Client Environment, Web Development in Server Environment, Web Applications Display,
                            Web Interfaces Design.</p>
                        <p>Associate Degree (Bac+2) is two years full-time.</p>
                        <hr>
                    </div>
                </div>
                <!-- Right Column -->
                <div class="w3-onethird">
                    <div class="w3-container w3-card w3-white w3-margin-bottom"></div>
                    <div class="w3-container w3-card w3-white">
                        <h2 class="w3-text-grey w3-padding-16"><i class="fa fa-heart fa-fw w3-margin-right w3-xxlarge w3-text-indigo"></i>Hobbies</h2>
                        <div class="w3-container">
                            <h5 class="w3-opacity"><b>Construction, Configuration and Equalization of SubWoofers,Speakers and Audio-Video equipment. </b></h5>
                            <h6 class="w3-text-indigo"><i class="fa fa-calendar fa-fw w3-margin-right"></i>2013 - <span class="w3-tag w3-indigo w3-round">Current</span></h6>
                            <p style="text-align:justify">SW ™ is a Startup for amateurs with a passion for Technology. Currently, it is the largest platform for Construction, Configuration and Equalization of SubWoofers, Speakers and Audio-Video equipment.</p>
                            <p style="text-align:justify"><strong>Backstory</strong></p>
                            <p style="text-align:justify">After making and equalize my own Subwoofers (do it yourself) for a while, I launched SW ™ as a personal project when I was living at London in 2013. In late 2014 I started to seriously consider working hard on SW ™ since its
                                growth was very promising, and I had many ideas that I thought would push the project even further. </p>
                            <p style="text-align:justify">SW ™ also offers all users the possibility of online calculating the design of a Subwoofer (Sealed or Bass Reflex) through a Software. </p>
                            <p style="text-align:justify"><strong>Rewards</strong></p>
                            <p>Plan the short-term and long-term roadmap for the project as a whole based on user feedback and new developments in the platform. </p>
                            <p style="text-align:justify">Working on SW ™ was how I grew as a developer: It motivated me to research and learn whatever it took to implement the features I wanted, and I had to hold myself up to decent engineering standards to keep the project maintainable.
                                When the project got bigger and more opinions started to surface. </p>
                            <p style="text-align:justify"><strong>Favorite moments</strong></p>
                            <p style="text-align:justify">Carlos is sound lover focused on the construction and equalization of Subwoofers, Speakers and Audio-Video equipment. </p>
                            <p style="text-align:justify">As a maintainer, most of the time you get pinged for problems in your project. Although it happens less often, it’s very heart-warming when users send you encouraging messages telling you how your project has made their work
                                more enjoyable and how grateful they are for that. I’m quite proud that all the private messages I got are the extremely positive type. </p>
                            <p style="text-align:justify"><strong>Responsiblities</strong></p>
                            <p style="text-align:justify">
                                <ul>
                                    <li>Carlos is in charge of the Programming and the management of the Community of Users.</li>
                                    <li>Programmed in PHP, MySQL, JavaScript, HTML5, CSS3 and Google Charts.</li>
                                </ul>
                            </p>
                            <p style="text-align:justify">Over time many wonderful community members have joined me, I’m extremely grateful to the community for making this a reality.</p>
                            </p>
                            <hr>
                        </div>
                        <div class="w3-container">
                            <h5 class="w3-opacity"><b>Maker Culture</b></h5>
                            <h6 class="w3-text-indigo"><i class="fa fa-calendar fa-fw w3-margin-right"></i>Since I was born - <span class="w3-tag w3-indigo w3-round">Current</span></h6>
                            <p style="text-align:justify">Maker culture emphasizes learning-through-doing (active learning) in a social environment. Maker culture emphasizes informal, networked, peer-led, and shared learning motivated by fun and self-fulfillment.</p>
                            <p style="text-align:justify">I started to build my own electric cars 1/10 scale after that build an explosion car of the same scale. I love discovering how things work.</p>
                            <hr>
                        </div>
                    </div>
                </div>
                <!-- Right Column -->
                <div class="w3-onethird">
                    <div class="w3-container w3-card w3-white w3-margin-bottom"></div>
                    <div class="w3-container w3-card w3-white">
                        <h2 class="w3-text-grey w3-padding-16"><i class="fa fa-file-word-o fa-fw w3-margin-right w3-xxlarge w3-text-indigo"></i>KeyWords</h2>
                        <div class="w3-container">
                            <h5 class="w3-opacity"><b>SEO </b></h5>
                            <h6 class="w3-text-indigo"><i class="fa fa-calendar fa-fw w3-margin-right"></i>KeyWords - <span class="w3-tag w3-indigo w3-round">Seo</span></h6>
                            <p style="text-align:justify">Key Words: Criminal Law, Technology Law, Cybercrime, Privacy, Ransomware, Entrepreneurship, StartUps, Smart Contracts (Solidity), Technology Investment, Full Stack Developer, Front-end Developer, Back-end Developer, Programming
                                Languages: JAVA, PHP, JavaScript, Python, Go, C, C++, C# ... HTML5, CSS3, XML, XPATH, XQUERY, XLST, AJAX, JSON, SOAP, API REST ... Databases, SQL, MySQL, Oracle, PL/SQL, MongoDB, SQLite ... Linux, Apple, Windows Server
                                ... NetWork, Routing and Switching, CCNA, Cisco Packet Tracert ... Scripting (Bash, PowerShell) ... Android, Swift ... Virtualization Software (VMWare, VirtualBox, Dockers, Vagrant) ... AWS, Google Cloud, Azure ... FrameWorks/Libraries
                                (Bootstrap, FlexBox, jQuery, Django, Nodejs) ... IDEs: NetBeans, Eclipse, Sublime Text3, Atom ... Git, SVN ... repository GitHub</p>
                            <hr>
                        </div>
                    </div>
                </div>
                <!-- End Right Column -->
            </div>
            <!-- End Grid -->
        </div>
        <!-- End Page Container -->
        <footer class="w3-container w3-indigo w3-center w3-margin-top">
            <p>Find me on social media</p><i class="fa fa-facebook-official w3-hover-opacity"></i><i class="fa fa-instagram w3-hover-opacity"></i><i class="fa fa-snapchat w3-hover-opacity"></i><i class="fa fa-pinterest-p w3-hover-opacity"></i><i class="fa fa-twitter w3-hover-opacity"></i>
            <i class="fa fa-linkedin w3-hover-opacity"></i>
            </br>
            <p class="social"><a style="text-decoration: none" href="http://www.achoweb.es" target="_blank" rel=”noopener noreferrer“>Design by Achoweb</a></p>
        </footer>
</body>

</html>
    """
    return HTMLResponse(content=html_content, status_code=200)


@app.get("/web/", response_class=HTMLResponse)
async def read_items():
    return generate_html_response()
