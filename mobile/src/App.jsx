import { StatusBar } from 'expo-status-bar';
import React from 'react';
import { View } from 'react-native';
import Greeting from './components/common/Greeting';
import globalStyles from './themes/styles';

export default function App() {
  return (
    <View style={globalStyles.container}>
      <Greeting />
      <StatusBar style="auto" />
    </View>
  );
}
