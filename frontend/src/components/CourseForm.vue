<template>
  <v-card class="mb-4" elevation="2">
    <v-card-title>Create Course</v-card-title>
    <v-card-text>
      <v-form v-model="formIsValid" @submit.prevent="submit" class="px-4 py-2">
        <v-row dense>
          <v-col cols="12" sm="6" md="4">
            <v-text-field
              v-model="name"
              label="Course Name"
              outlined
              dense
              clearable
              :rules="[requiredRule]"
            />
          </v-col>

          <v-col cols="12" sm="6" md="4">
            <v-text-field
              v-model="duration"
              label="Duration"
              outlined
              dense
              clearable
              :rules="[requiredRule]"
            />
          </v-col>

          <v-col cols="12" sm="6" md="4">
            <v-text-field
              v-model="fee"
              label="Fee"
              type="number"
              outlined
              dense
              clearable
              class="no-shadow"
              :rules="[requiredRule, feeRule]"
            />
          </v-col>
        </v-row>

        <v-row justify="end">
          <v-col cols="auto">
            <v-btn type="submit" color="primary" class="mt-2" elevation="2" :disabled="!formIsValid">
              Submit
            </v-btn>
          </v-col>
        </v-row>
      </v-form>
    </v-card-text>
  </v-card>
</template>

<script setup>
import { ref } from 'vue'

const emit = defineEmits(['refresh'])

const name = ref('')
const duration = ref('')
const fee = ref('')
const formIsValid = ref(false)

// Validation rules
const requiredRule = v => !!v || 'This field is required'
const feeRule = v => (v && parseInt(v) > 0) || 'Fee must be greater than 0'

const submit = async () => {
  if (!formIsValid.value) return

  try {
    const res = await fetch('http://localhost:5000/courses', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        name: name.value,
        duration: duration.value,
        fee: parseInt(fee.value)
      })
    })

    const result = await res.json()

    if (res.ok) {
      name.value = ''
      duration.value = ''
      fee.value = ''
      emit('refresh')
      alert('Course created successfully!')
    } else {
      alert(result.error || 'Failed to create course')
    }
  } catch (error) {
    alert('Network or server error. Please try again later.')
    console.error(error)
  }
}
</script>

<style>
.no-shadow {
  box-shadow: none !important;
}
</style>
