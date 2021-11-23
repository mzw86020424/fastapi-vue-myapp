<template>
<v-form v-model="valid">
  <v-container>
    <v-row>
      <v-col cols="12" md="4">
        <v-text-field
        v-model="get_key"
        label="GET key"
        ></v-text-field>
        <v-btn
        color="primary"
        text
        @click="get_data"
        >get</v-btn>
      </v-col>

      <v-col cols="12" md="4">
        <v-text-field
        v-model="post_key"
        label="POST key"
        ></v-text-field>
        <v-text-field
        v-model="post_val"
        label="POST value"
        ></v-text-field>
        <v-btn
        color="primary"
        text
        @click="post_data"
        >post</v-btn>
      </v-col>

    </v-row>
    <h1>{{ result }}</h1>
  </v-container>
</v-form>
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
        .get("/data/", {
          params: {
            key: this.get_key
          }
        })
        .then(
          response => {
            this.result = response.data;
            console.log(response);
          }
        )
        .catch(
          error => {
            this.result = "GETエラー";
            console.log(error);
          }
        );
    },
    post_data() {
      axios
        .post("/data/", {
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