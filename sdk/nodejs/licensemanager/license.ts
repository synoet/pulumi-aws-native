// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs } from "../types";
import * as utilities from "../utilities";

/**
 * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-licensemanager-license.html
 */
export class License extends pulumi.CustomResource {
    /**
     * Get an existing License resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): License {
        return new License(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:licensemanager:License';

    /**
     * Returns true if the given object is an instance of License.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is License {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === License.__pulumiType;
    }

    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-licensemanager-license.html#cfn-licensemanager-license-beneficiary
     */
    public readonly beneficiary!: pulumi.Output<string | undefined>;
    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-licensemanager-license.html#cfn-licensemanager-license-consumptionconfiguration
     */
    public readonly consumptionConfiguration!: pulumi.Output<outputs.licensemanager.LicenseConsumptionConfiguration>;
    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-licensemanager-license.html#cfn-licensemanager-license-entitlements
     */
    public readonly entitlements!: pulumi.Output<outputs.licensemanager.LicenseEntitlement[]>;
    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-licensemanager-license.html#cfn-licensemanager-license-homeregion
     */
    public readonly homeRegion!: pulumi.Output<string>;
    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-licensemanager-license.html#cfn-licensemanager-license-issuer
     */
    public readonly issuer!: pulumi.Output<outputs.licensemanager.LicenseIssuerData>;
    public /*out*/ readonly licenseArn!: pulumi.Output<string>;
    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-licensemanager-license.html#cfn-licensemanager-license-licensemetadata
     */
    public readonly licenseMetadata!: pulumi.Output<outputs.licensemanager.LicenseMetadata[] | undefined>;
    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-licensemanager-license.html#cfn-licensemanager-license-licensename
     */
    public readonly licenseName!: pulumi.Output<string>;
    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-licensemanager-license.html#cfn-licensemanager-license-productname
     */
    public readonly productName!: pulumi.Output<string>;
    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-licensemanager-license.html#cfn-licensemanager-license-productsku
     */
    public readonly productSKU!: pulumi.Output<string | undefined>;
    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-licensemanager-license.html#cfn-licensemanager-license-status
     */
    public readonly status!: pulumi.Output<string | undefined>;
    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-licensemanager-license.html#cfn-licensemanager-license-validity
     */
    public readonly validity!: pulumi.Output<outputs.licensemanager.LicenseValidityDateFormat>;
    public /*out*/ readonly version!: pulumi.Output<string>;

    /**
     * Create a License resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: LicenseArgs, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.consumptionConfiguration === undefined) && !opts.urn) {
                throw new Error("Missing required property 'consumptionConfiguration'");
            }
            if ((!args || args.entitlements === undefined) && !opts.urn) {
                throw new Error("Missing required property 'entitlements'");
            }
            if ((!args || args.homeRegion === undefined) && !opts.urn) {
                throw new Error("Missing required property 'homeRegion'");
            }
            if ((!args || args.issuer === undefined) && !opts.urn) {
                throw new Error("Missing required property 'issuer'");
            }
            if ((!args || args.licenseName === undefined) && !opts.urn) {
                throw new Error("Missing required property 'licenseName'");
            }
            if ((!args || args.productName === undefined) && !opts.urn) {
                throw new Error("Missing required property 'productName'");
            }
            if ((!args || args.validity === undefined) && !opts.urn) {
                throw new Error("Missing required property 'validity'");
            }
            inputs["beneficiary"] = args ? args.beneficiary : undefined;
            inputs["consumptionConfiguration"] = args ? args.consumptionConfiguration : undefined;
            inputs["entitlements"] = args ? args.entitlements : undefined;
            inputs["homeRegion"] = args ? args.homeRegion : undefined;
            inputs["issuer"] = args ? args.issuer : undefined;
            inputs["licenseMetadata"] = args ? args.licenseMetadata : undefined;
            inputs["licenseName"] = args ? args.licenseName : undefined;
            inputs["productName"] = args ? args.productName : undefined;
            inputs["productSKU"] = args ? args.productSKU : undefined;
            inputs["status"] = args ? args.status : undefined;
            inputs["validity"] = args ? args.validity : undefined;
            inputs["licenseArn"] = undefined /*out*/;
            inputs["version"] = undefined /*out*/;
        } else {
            inputs["beneficiary"] = undefined /*out*/;
            inputs["consumptionConfiguration"] = undefined /*out*/;
            inputs["entitlements"] = undefined /*out*/;
            inputs["homeRegion"] = undefined /*out*/;
            inputs["issuer"] = undefined /*out*/;
            inputs["licenseArn"] = undefined /*out*/;
            inputs["licenseMetadata"] = undefined /*out*/;
            inputs["licenseName"] = undefined /*out*/;
            inputs["productName"] = undefined /*out*/;
            inputs["productSKU"] = undefined /*out*/;
            inputs["status"] = undefined /*out*/;
            inputs["validity"] = undefined /*out*/;
            inputs["version"] = undefined /*out*/;
        }
        if (!opts.version) {
            opts = pulumi.mergeOptions(opts, { version: utilities.getVersion()});
        }
        super(License.__pulumiType, name, inputs, opts);
    }
}

/**
 * The set of arguments for constructing a License resource.
 */
export interface LicenseArgs {
    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-licensemanager-license.html#cfn-licensemanager-license-beneficiary
     */
    beneficiary?: pulumi.Input<string>;
    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-licensemanager-license.html#cfn-licensemanager-license-consumptionconfiguration
     */
    consumptionConfiguration: pulumi.Input<inputs.licensemanager.LicenseConsumptionConfigurationArgs>;
    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-licensemanager-license.html#cfn-licensemanager-license-entitlements
     */
    entitlements: pulumi.Input<pulumi.Input<inputs.licensemanager.LicenseEntitlementArgs>[]>;
    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-licensemanager-license.html#cfn-licensemanager-license-homeregion
     */
    homeRegion: pulumi.Input<string>;
    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-licensemanager-license.html#cfn-licensemanager-license-issuer
     */
    issuer: pulumi.Input<inputs.licensemanager.LicenseIssuerDataArgs>;
    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-licensemanager-license.html#cfn-licensemanager-license-licensemetadata
     */
    licenseMetadata?: pulumi.Input<pulumi.Input<inputs.licensemanager.LicenseMetadataArgs>[]>;
    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-licensemanager-license.html#cfn-licensemanager-license-licensename
     */
    licenseName: pulumi.Input<string>;
    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-licensemanager-license.html#cfn-licensemanager-license-productname
     */
    productName: pulumi.Input<string>;
    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-licensemanager-license.html#cfn-licensemanager-license-productsku
     */
    productSKU?: pulumi.Input<string>;
    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-licensemanager-license.html#cfn-licensemanager-license-status
     */
    status?: pulumi.Input<string>;
    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-licensemanager-license.html#cfn-licensemanager-license-validity
     */
    validity: pulumi.Input<inputs.licensemanager.LicenseValidityDateFormatArgs>;
}
