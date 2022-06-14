import './App.css';
import 'antd/dist/antd.css';
import RouterApp from './RouterApp';
import {ApolloClient, InMemoryCache, ApolloProvider} from "@apollo/client";

const client = new ApolloClient({
  uri: 'http://localhost:8000',
  cache: new InMemoryCache(),
});

function App() {
  return (
      <ApolloProvider client={client}>
        <RouterApp />
      </ApolloProvider>
  );
}

export default App;
