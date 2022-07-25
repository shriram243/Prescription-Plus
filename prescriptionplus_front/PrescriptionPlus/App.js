import React, {useState} from "react";
import {View, 
  Text,
  StyleSheet, 
  FlatList, 
  Alert,
  TextInput,
Pressable} from "react-native";
import Header from "./components/header";

import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';
import { TouchableOpacity } from "react-native-gesture-handler";
import Icon from "react-native-vector-icons/Feather";
import SearchBar from "react-native-dynamic-search-bar";
import axios from "axios";

const Stack = createStackNavigator();







function Main_screen({navigation}) {
  const onPressHandler = () =>{
    navigation.navigate('create_Rx_screen')
  }
  return (
    <View>
      {/* <Pressable onPress={onPressHandler} style={styles.createRxbutton}>
        <Text style={styles.text}>
          Create Rx
        </Text>
      </Pressable> */}
      <TouchableOpacity onPress={()=>onPressHandler()} style={styles.createRxbutton}>
        <Text style={styles.text}>
          Create Rx
        </Text>
      </TouchableOpacity>
    </View>
  )
}


function Create_Rx({navigation}) {
  const onPressHandler = (title) =>{
    // console.log("+++++++++tilte+++++++++"+title)
    if(title == 'Complaints'){
      navigation.navigate('Add complaints')
    }
    else if(title == 'Rx'){
      navigation.navigate('Add Rx')
    }
    else if(title == 'Advice'){
      navigation.navigate('Add advice')
    }
    else if(title == 'Tests requested'){
      navigation.navigate('Add test')
    }
    else if(title == 'Follow up date'){
      navigation.navigate('Add follow up date')
    }
    else{
      navigation.navigate('create_Rx_screen')
    }
  }

  const [RxItems, setRxItems] = useState([
    {title: 'Complaints'},
    {title: 'Rx'},
    {title: 'Advice'},
    {title: 'Tests requested'},
    {title: 'Follow up date'},
  ]);
  return (
    <FlatList
      disableScrollViewPanResponder = {true}
       keyExtractor={(item, index) => index.toString()}
       data={RxItems}
       renderItem={({ item }) => (
         <TouchableOpacity style={styles.item} onPress={()=>onPressHandler(item.title)}>
           <Text style={styles.text}>{item.title}</Text>
           <Icon name="plus-circle" size={70} style={styles.text}/>
         </TouchableOpacity>
       )}
      //  refreshControl={
      //    <RefreshControl
      //      refreshing={Refreshing}
      //      onRefresh={onRefresh}
      //    />
      //  }
    />
  )
}




function Add_complaints({navigation}) {
  const getSymptoms = async (data) =>{
    const param = {val:data};
    var url = 'http://172.29.204.211:5000/search/symptoms?data='+data
    // var url = 'https://jsonplaceholder.typicode.com/todos/1'
    
    try{
      // let formData = new FormData();
      // formData.append("category",category)
      console.log(url)
        await fetch(url,
        {
            method : 'GET',
            headers : {'content-type': 'application/x-www-form-urlencoded'}

        })
        .then(function (response) {
          console.log(response)
            return response.json();})
        .then(function (result) {            
            // setDocumentsList(result["data"]);
            console.log('returned json',result["data"]);
            //console.log('response data', documentsList)
            // setLoading(true)

        }).catch(function (error) {
            console.log("-------- error ------- "+error);
            alert("result:"+error)
         });
            
            
        
            
        
    }
    catch(e){
        console.log(e)
    }
  }
  const onPressHandler = () =>{
    navigation.goBack();
  }
  return (
    <SearchBar
  placeholder="Search here"
  onPress={() => alert("onPress")}
  onChangeText={(text) => {getSymptoms(text)}}
/>

  )
}
function Add_Rx({navigation}) {
  const onPressHandler = () =>{
    navigation.goBack();
  }
  return (
    <SearchBar
  placeholder="Search here"
  onPress={() => alert("onPress")}
  onChangeText={(text) => console.log(text)}
/>

  )
}

function Add_test({navigation}) {
  const onPressHandler = () =>{
    navigation.goBack();
  }
  return (
    <SearchBar
  placeholder="Search here"
  onPress={() => alert("onPress")}
  onChangeText={(text) => console.log(text)}
/>

  )
}

function Add_advice({navigation}) {
  const [Advice, setAdvice] = useState('');
  const onChange = textValue => setAdvice(textValue);
  const onPressHandler = () =>{
    navigation.goBack();
  }
  return (
    <View>
      <TextInput placeholder="Add advice for the patient" onChangeText={onChange}/>
      <TouchableOpacity onPress={()=>onPressHandler()} style={styles.createRxbutton}>
        <Text style={styles.text}>
          Add Advice
        </Text>
      </TouchableOpacity>
    </View>

  )
}

function Add_follow_up({navigation}) {
  const [Advice, setAdvice] = useState('');
  const onChange = textValue => setAdvice(textValue);
  const onPressHandler = () =>{
    navigation.goBack();
  }
  return (
    <View>
      <Text>Add the follow up date</Text>
    </View>

  )
}




const App =()=>{

  
  return(<View style={styles.container}>
    <Header/>
    <NavigationContainer >
      <Stack.Navigator screenOptions={{
        headerShown: true
      }}>
        <Stack.Screen 
        name="main_screen"
        component={Main_screen}
        />
        <Stack.Screen 
        name="create_Rx_screen"
        component={Create_Rx}
        />
        <Stack.Screen 
        name="Add complaints"
        component={Add_complaints}
        />
        <Stack.Screen 
        name="Add Rx"
        component={Add_Rx}
        />
        <Stack.Screen 
        name="Add advice"
        component={Add_advice}
        />
        <Stack.Screen 
        name="Add test"
        component={Add_test}
        />
        <Stack.Screen 
        name="Add follow up date"
        component={Add_follow_up}
        />

      </Stack.Navigator>
    </NavigationContainer>
  </View>);
}



const styles = StyleSheet.create({
  body: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
  text: {
    fontSize: 40,
    fontWeight: 'bold',
    margin: 10,
  },
  container: {
    flex: 1,
  },
  createRxbutton: {
    flexDirection: 'row-reverse',
    backgroundColor: 'darkslateblue',
    margin: 20,
    alignContent: 'center',
    justifyContent: 'center',
    borderRadius: 400,
    // justifyContent: 'flex-start',
    
  },
  item: {
    margin: 1,
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'flex-start',
    borderColor: 'black',
    borderWidth: 1,
  },
  
 
})

export default App;   
