#include <stdio.h>
#include <jsoncpp/json/json.h>
// #include <jsoncpp/json/reader.h>
// #include <jsoncpp/json/writer.h>
// #include <jsoncpp/json/value.h>
#include <string>

int main( int argc, const char* argv[] )
{

    std::string strJson = "{\"robo1\":{\"x\":1,\"y\":2}, \"robo2\":{\"x\":3,\"y\":4}}"; // need escape the quotes

    Json::Value root;   
    Json::Reader reader;
    bool parsingSuccessful = reader.parse( strJson.c_str(), root );     //parse process
    if ( !parsingSuccessful )
    {
        std::cout  << "Failed to parse"
               << reader.getFormattedErrorMessages();
        return 0;
    }
    std::cout << root.get("robo1", "A Default Value if not exists" ) << std::endl;
    std::cout << root["robo1"]["x"] << std::endl;
    return 0;
}