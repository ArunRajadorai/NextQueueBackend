import AdaptableCard from '@/components/shared/AdaptableCard'
import { FormItem } from '@/components/ui/Form'
import Input from '@/components/ui/Input'
import Select from '@/components/ui/Select'
import CreatableSelect from 'react-select/creatable'
import { Field, FormikErrors, FormikTouched, FieldProps } from 'formik'
import { DatePicker } from '@/components/ui'
import dayjs from 'dayjs'

type FormFieldsName = {
    shopState?: string
    shopCountry?: string
}

type DropdownFieldsProps = {
    touched: FormikTouched<FormFieldsName>
    errors: FormikErrors<FormFieldsName>
    values: {
        shopCountry: string
        [key: string]: unknown
    }
}


const countries = [
    { label: "United States", value: "United States" },
    { label: "Canada", value: "Canada" },
    { label: "United Kingdom", value: "United Kingdom" },
    { label: "Australia", value: "Australia" },
    { label: "Germany", value: "Germany" },
    { label: "France", value: "France" },
    { label: "India", value: "India" },
    { label: "Japan", value: "Japan" },
    { label: "Brazil", value: "Brazil" },
    { label: "Mexico", value: "Mexico" },
    { label: "China", value: "China" },
    { label: "Russia", value: "Russia" },
    { label: "South Africa", value: "South Africa" },
    { label: "Spain", value: "Spain" },
    { label: "Italy", value: "Italy" }
]

const DropdownFields = (props: DropdownFieldsProps) => {
    const { values = { shopCountry: '', shopState: '' },
        touched, errors } = props
    return (
        <AdaptableCard divider isLastChild className="mb-4">
            <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                <div className="col-span-1">
                    <FormItem
                        label="State/Region"
                        invalid={(errors.shopState && touched.shopState) as boolean}
                        errorMessage={errors.shopState}
                    >
                        <Field
                            type="text"
                            autoComplete="off"
                            name="shopState"
                            placeholder="State"
                            component={Input}
                        />
                    </FormItem>
                </div>
                <div className="col-span-1">
                    <FormItem
                        label="Country1"
                        invalid={
                            (errors.shopCountry && touched.shopCountry) as boolean
                        }
                        errorMessage={errors.shopCountry}
                    >
                        <Field name="shopCountry">
                            {({ field, form }: FieldProps) => (
                                <Select
                                    field={field}
                                    form={form}
                                    options={countries}
                                    value={countries.filter(
                                        (shopCountry) =>
                                            shopCountry.value ===
                                            values.shopCountry
                                    )}
                                    onChange={(option) =>
                                        form.setFieldValue(
                                            field.name,
                                            option?.value
                                        )
                                    }
                                />
                            )}
                        </Field>
                    </FormItem>
                </div>
            </div>
        </AdaptableCard>
    )
}

export default DropdownFields;
