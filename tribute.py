# tributepage.html

import webbrowser

f = open('tributepage.html', 'w')

html = """
<!doctype html>
<html lang="en">

    <head>

        <!-- CSS file for surveyform.html -->
            <link rel="stylesheet" href="css_tribute.css">
    </head>

    <body>
     <h1 id="title">This is an exercise from freecodecamp.org
     <br>Select Tribute Page from the Test Suite</h1>
            <br><br>
        <main id="main">
        <h1 id="title"> Sean Connery</h1>
            
            <div id="img-div">
                
        <img id="image" src="https://upload.wikimedia.org/wikipedia/commons/d/de/Sean_Connery%2C_Bestanddeelnr_932-7859.jpg" 
                
            alt="Sean Connery, Bestanddeelnr 932-7859.jpg">
            
            <a  href="https://commons.wikimedia.org/wiki/File:Sean_Connery,_Bestanddeelnr_932-7859.jpg"> <br> Rob Bogaerts / Anefo</a>, CC0, via Wikimedia Commons      
            
            <figcaption id="img-caption">Fig. 1, Sean Connery</figcaption>
            <br><br>
            <p id="tribute-info">Sean Connery was a renowned actor. He was well known for all his James Bond movies, not to mention the varieties of roles he played in many films.
        <br>        
        <br>
                Some of his famous movies which he was known for were Dr. No(1962), Goldfinger(1964) and Diamonds are Forever(1971) James Bond movies. He also portrayed a few roles in other films such as The Hunt for Red October(1990), Robin Hood: Prince of Thieves(1991) and The Rock(1996), just to name a few. Honorable mentions were The Untouchables(1987) and Indiana Jones and the Last Crusade(1989).</p>
            <br><br>
            Read more about Sean Connery in
            <a id="tribute-link" href="https://en.wikipedia.org/wiki/Sean_Connery" target="_blank"> Wikipedia</a>
            
            </div>
        
        </main>
        
           <script src="https://cdn.freecodecamp.org/testable-projects-fcc/v1/bundle.js"></script>
    </body>

</html>
    
  """

f.write(html)
f.close()

webbrowser.open_new_tab('tributepage.html')
