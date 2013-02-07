<html>
<head>
    <title>{{title}}</title>
</head>
<body>
    %for post in posts:
        <h1>{{post['titulo']}}</h1>
        <p>{{post['conteudo']}}</p>
    %end
</body>
