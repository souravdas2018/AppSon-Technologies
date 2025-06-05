<template>
  <v-card elevation="3" class="pa-6 rounded-lg">
    <v-card-title class="text-h6 mb-4">Register New Student</v-card-title>

    <v-form v-model="formIsValid" @submit.prevent="submit">
      <v-container fluid>
        <v-row dense>
          <v-col cols="12" sm="6">
            <v-text-field
              v-model="first_name"
              label="First Name"
              outlined
              dense
              clearable
              :rules="[requiredRule]"
            />
          </v-col>

          <v-col cols="12" sm="6">
            <v-text-field
              v-model="last_name"
              label="Last Name"
              outlined
              dense
              clearable
              :rules="[requiredRule]"
            />
          </v-col>

          <v-col cols="12" sm="6">
            <v-text-field
              v-model="dob"
              label="Date of Birth"
              outlined
              dense
              clearable
              type="date"
              :rules="[requiredRule, validDateRule]"
            />
          </v-col>

          <v-col cols="12" sm="6">
            <v-text-field
              v-model="address"
              label="Address"
              outlined
              dense
              clearable
              :rules="[requiredRule]"
            />
          </v-col>

          <v-col cols="12">
            <v-select
              v-model="course_id"
              :items="courses.map(c => ({ title: c.name, value: c.id }))"
              label="Course"
              outlined
              dense
              clearable
              :rules="[requiredRule]"
            />
          </v-col>

          <v-col cols="12" class="text-end">
            <v-btn
              type="submit"
              color="green"
              class="mt-2"
              rounded
              :disabled="!formIsValid"
            >Register</v-btn>
          </v-col>
        </v-row>
      </v-container>
    </v-form>
  </v-card>
</template>

<script setup>
import { ref } from 'vue'

const props = defineProps(['courses'])
const emit = defineEmits(['refresh'])

const first_name = ref('')
const last_name = ref('')
const dob = ref('')
const address = ref('')
const course_id = ref(null)
const formIsValid = ref(false)
const loading = ref(false)

const snackbar = ref({
  show: false,
  message: '',
  color: ''
})

// Validation rules
const requiredRule = v => !!v || 'This field is required'

const validDateRule = v => {
  if (!v) return true
  // Check valid YYYY-MM-DD and valid date
  const regex = /^\d{4}-\d{2}-\d{2}$/
  if (!regex.test(v)) return 'Date must be in YYYY-MM-DD format'

  const d = new Date(v)
  if (isNaN(d.getTime())) return 'Invalid date'

  return true
}

const submit = async () => {
  const form = ref('form').value
  if (!form.validate()) return

  loading.value = true

  try {
    const res = await fetch('http://localhost:5000/students', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        first_name: first_name.value,
        last_name: last_name.value,
        dob: dob.value,
        address: address.value,
        course_id: course_id.value
      })
    })

    const data = await res.json()

    if (res.ok) {
      first_name.value = ''
      last_name.value = ''
      dob.value = ''
      address.value = ''
      course_id.value = null

      // reset validation
      form.resetValidation()

      emit('refresh')

      snackbar.value = {
        show: true,
        message: 'Student registered successfully!',
        color: 'success'
      }
    } else {
      snackbar.value = {
        show: true,
        message: data.error || 'Failed to register student.',
        color: 'error'
      }
    }
  } catch (err) {
    snackbar.value = {
      show: true,
      message: 'Network error. Please try again later.',
      color: 'error'
    }
    console.error(err)
  } finally {
    loading.value = false
  }
}
</script>