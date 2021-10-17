<template>
  <div class="hello">
    <h1>APIにリクエスト</h1>
    <input type="text" v-model="get_key" />
    <input @click="get_data" type="button" value="GET" />
    <br />
    <input type="text" v-model="post_key" />
    <input type="text" v-model="post_val" />
    <input @click="post_data" type="button" value="POST" />
    <p>{{ result }}</p>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "HelloWorld",
  data() {
    return {
      get_key: "",
      post_key: "",
      post_val: "",
      result: ""
    };
  },
  methods: {
    get_data() {
      axios
        .get("http://127.0.0.1:8000/data/", {
          params: {
            key: this.get_key
          }
        })
        .then(
          function(response) {
            this.result = response.data;
            console.log(response);
          }.bind(this)
        )
        .catch(
          function(error) {
            this.result = "GETエラー";
            console.log(error);
          }.bind(this)
        );
    },
    post_data() {
      axios
        .post("http://127.0.0.1:8000/data/", {
          name: this.post_key,
          mean: this.post_val
        })
        .then(
          function(response) {
            this.result = "保存しました";
            console.log(response);
          }.bind(this)
        )
        .catch(
          function(error) {
            this.result = "POSTエラー";
            console.log(error);
          }.bind(this)
        );
    }
  }
};
</script>