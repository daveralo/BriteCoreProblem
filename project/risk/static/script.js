// Text input field component
const textInput = {
  props: {
    field: { required: true },
    data: { required: true }
  },
  
  template: `
  <div class="form-control">
    <label>{{ field.label }}</label>
    <input class="input" type="text" :placeholder="field.placeholder" v-model="data.value">
  </div>
  `
};

// Checkbox input field component
const checkboxInput = {
  props: {
    field: { required: true },
    data: { required: true }
  },
  
  template: `
  <div class="form-control">
    <label>{{ field.label }}</label>
    <label class="input">
      <input type="checkbox" v-model="data.value">
      {{ field.placeholder }}
    </label>
  </div>
  `
};

// Dynamic form component
const vForm = {
  template: `
  <div class="VueForm">
    <template v-for="field in schema.fields">
      <component :is="field.type" :field="field" :data.sync="data[field.name]"></component>
    </template>
  </div>
  `,
  
  components: {
    textInput: textInput,
    checkboxInput: checkboxInput
  },
  
  props: {
    schema: { required: true },
    data: { required: true }
  }
};

Vue.component('v-form', vForm);

// Root Vue instance
const app =new Vue({
  el: '#app',
  
  data: {
    formSchema: {
      fields: [
        {
          type: 'text-input',
          name: 'first_name',
          label: 'First name',
          placeholder: 'Enter first namee'
        },
        {
          type: 'text-input',
          name: 'last_name',
          label: 'Last name',
          placeholder: 'Enter last name'
        },
        {
          type: 'checkbox-input',
          name: 'is_admin',
          label: 'Administrator',
          placeholder: 'Sure, why noyt'
        }
      ]
    },
    formData: {
      first_name: {
        value: 'Daniel'
      },
      last_name: {
        value: 'Doe'
      },
      is_admin: {
        value: true
      }
    }
  }
});