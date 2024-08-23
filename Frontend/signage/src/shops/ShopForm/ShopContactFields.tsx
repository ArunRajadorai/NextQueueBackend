import AdaptableCard from '@/components/shared/AdaptableCard'
import { FormItem } from '@/components/ui/Form'
import Input from '@/components/ui/Input'
// import { NumericFormat, NumericFormatProps } from 'react-number-format'
import {
    Field, FieldProps,
    FormikErrors,
    FormikTouched,
    // FieldProps,
    // FieldInputProps,
} from 'formik'
import Select from "@/components/ui/Select";
// import type { ComponentType } from 'react'
// import type { InputProps } from '@/components/ui/Input'

type FormFieldsName = {
    shopEmail?: string
    shopPhone?: string
    shopAddress1?: string
    shopAddress2?: string
    shopTown?: string
    shopPostalcode?: string
    shopState?: string
    shopCountry?: string
}

type ShopContactFieldsProps = {
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

const ShopContactFields = (props: ShopContactFieldsProps) => {  const { values = { shopCountry: '', shopState: '' },
        touched, errors } = props

    return (
        <AdaptableCard divider className="mb-4">
            <h5>Shop Contact Details</h5>
            <p className="mb-6">Section to config Shop contact information</p>
            <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                <div className="col-span-1">
                    <FormItem
                        label="Email"
                        invalid={(errors.shopEmail && touched.shopEmail) as boolean}
                        errorMessage={errors.shopEmail}
                    >
                        <Field
                            type="text"
                            autoComplete="off"
                            name="shopEmail"
                            placeholder="Email"
                            component={Input}
                        />
                    </FormItem>
                </div>
                <div className="col-span-1">
                    <FormItem
                        label="Phone"
                        invalid={(errors.shopPhone && touched.shopPhone) as boolean}
                        errorMessage={errors.shopPhone}
                    >
                        <Field
                            type="text"
                            autoComplete="off"
                            name="shopPhone"
                            placeholder="Phone"
                            component={Input}
                        />
                    </FormItem>
                </div>
            </div>
            <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                <div className="col-span-1">
                    <FormItem
                        label="Address"
                        invalid={(errors.shopAddress1 && touched.shopAddress1) as boolean}
                        errorMessage={errors.shopAddress1}
                    >
                        <Field
                            type="text"
                            autoComplete="off"
                            name="shopAddress1"
                            placeholder="Street Address"
                            component={Input}
                        />
                    </FormItem>

                </div>
                <div className="col-span-1">
                    <FormItem
                        label="Address Line2"
                        invalid={(errors.shopAddress2 && touched.shopAddress2) as boolean}
                        errorMessage={errors.shopAddress2}
                    >
                        <Field
                            type="text"
                            autoComplete="off"
                            name="shopAddress2"
                            placeholder="Street Address Line 2"
                            component={Input}
                        />
                    </FormItem>
                </div>
            </div>
            <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                <div className="col-span-1">
                    <FormItem
                        label="Town/City"
                        invalid={(errors.shopTown && touched.shopTown) as boolean}
                        errorMessage={errors.shopTown}
                    >
                        <Field
                            type="text"
                            autoComplete="off"
                            name="shopTown"
                            placeholder="Town/City"
                            component={Input}
                        />
                    </FormItem>

                </div>
                <div className="col-span-1">
                    <FormItem
                        label="Postal Code"
                        invalid={(errors.shopPostalcode && touched.shopPostalcode) as boolean}
                        errorMessage={errors.shopPostalcode}
                    >
                        <Field
                            type="text"
                            autoComplete="off"
                            name="shopPostalcode"
                            placeholder="Postal/Zip Code"
                            component={Input}
                        />
                    </FormItem>
                </div>
            </div>
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
                        label="Country"
                        invalid={
                            (errors.shopCountry && touched.shopCountry) as boolean
                        }
                        errorMessage={errors.shopCountry}
                    >
                        <Field name="country">
                            {({field, form}: FieldProps) => (
                                <Select
                                    field={field}
                                    form={form}
                                    options={countries}
                                    value={countries.filter(
                                        (shopCountry) =>
                                            shopCountry.value ===
                                            values.country
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

export default ShopContactFields
