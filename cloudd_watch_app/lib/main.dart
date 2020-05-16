import 'package:cloudd_watch_app/aws_resource_client.dart';
import 'package:dio/dio.dart';
import 'package:flutter/material.dart';

void main() {
  runApp(CloudWatchApp());
}

class CloudWatchApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      theme: ThemeData(
        primarySwatch: Colors.blue,
        visualDensity: VisualDensity.adaptivePlatformDensity,
      ),
      home: HomePage(),
    );
  }
}

class HomePage extends StatefulWidget {
  HomePage({Key key}) : super(key: key);

  @override
  _HomePageState createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: SafeArea(
        child: Container(
           child: Column(
             mainAxisAlignment: MainAxisAlignment.center,
             children: [
              Row(
                mainAxisAlignment: MainAxisAlignment.center,
                children: [
                  Text(
                    "AWS EC2 Instances",
                    style: TextStyle(
                      color: Colors.black,
                      fontSize: 24.0,
                    ),
                  )
                ],
              ),
               FutureBuilder(
                 future: this._fetchData(),
                 builder: (context, snapshot) {
                   switch (snapshot.connectionState) {
                     case ConnectionState.none:
                     case ConnectionState.waiting:
                     case ConnectionState.active:
                      return Center(child: CircularProgressIndicator(
                        strokeWidth: 1.0,
                      ),);
                    case ConnectionState.done:
                      // handle dio erros here
                      Response response = snapshot.data;
                      var stoppedAWS = response.data.where((i) => i['status']['Code'] == 80).toList();
                      var runningAWS = response.data.where((i) => i['status']['Code'] == 16).toList();
                      print(response);
                      return Center(
                        child: Column(
                          mainAxisAlignment: MainAxisAlignment.center,
                          children: [
                            Row(
                              mainAxisAlignment: MainAxisAlignment.center,
                              children: [
                                Text(
                                  "Running: "+runningAWS.length.toString(),
                                  style: TextStyle(
                                    color: Colors.green,
                                    fontSize: 18.0
                                  ),
                                )
                              ],
                            ),
                            Row(
                              mainAxisAlignment: MainAxisAlignment.center,
                              children: [
                                Text(
                                  "Stopped: "+stoppedAWS.length.toString(),
                                  style: TextStyle(
                                    color: Colors.red,
                                    fontSize: 18.0
                                  ),
                                )
                              ],
                            ),
                          ]
                        ),
                      );
                    default:
                      return Center(child: Text("Default"));
                   }
                 },
               ),
             ],
           ),
        ),
      ),
    );
  }

  _fetchData() async {
    var awsRequests = AWSRequests();
    return await awsRequests.ec2Machines;
  }
}