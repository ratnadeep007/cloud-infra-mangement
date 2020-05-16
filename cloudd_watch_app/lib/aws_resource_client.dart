import 'package:dio/dio.dart';


class AWSRequests { 
  Dio dio = Dio();
  String url = "Enter lambda url here";

  get ec2Machines async {
    try {
      Response response = await dio.get(url+"ec2");
      return response;
    } catch(e) {
      print(e);
    }
  }
}