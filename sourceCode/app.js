let express = require( 'express' );
let app = express();
let server = require( 'http' ).Server( app );
let io = require( 'socket.io' )( server );
let stream = require( './ws/stream' );
let path = require( 'path' );
let favicon = require( 'serve-favicon' );
let mysql = require('mysql');
let bodyParser = require('body-parser');
const cors = require('cors');

app.use( favicon( path.join( __dirname, 'favicon.ico' ) ) );
app.use( '/assets', express.static( path.join( __dirname, 'assets' ) ) );
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({extended: true}));
app.use(cors());
app.set('view engine','html');
app.engine('html', require('ejs').renderFile);

// router
app.post( '/', ( req, res ) => {
    var userName = req.body.userName;
    console.log(userName);
    res.render(__dirname+'/index.html',{'userId': userName} );
} );

app.get( '/pose', (req, res) => {
    res.sendFile( __dirname + '/pose.html' );
} );

io.of( '/stream' ).on( 'connection', stream );

server.listen(3000);
