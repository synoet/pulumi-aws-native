// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource Schema for AWS::ServiceCatalog::CloudFormationProvisionedProduct
 */
export class CloudFormationProvisionedProduct extends pulumi.CustomResource {
    /**
     * Get an existing CloudFormationProvisionedProduct resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): CloudFormationProvisionedProduct {
        return new CloudFormationProvisionedProduct(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:servicecatalog:CloudFormationProvisionedProduct';

    /**
     * Returns true if the given object is an instance of CloudFormationProvisionedProduct.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is CloudFormationProvisionedProduct {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === CloudFormationProvisionedProduct.__pulumiType;
    }

    public readonly acceptLanguage!: pulumi.Output<enums.servicecatalog.CloudFormationProvisionedProductAcceptLanguage | undefined>;
    public /*out*/ readonly cloudformationStackArn!: pulumi.Output<string>;
    public readonly notificationArns!: pulumi.Output<string[] | undefined>;
    /**
     * List of key-value pair outputs.
     */
    public /*out*/ readonly outputs!: pulumi.Output<any>;
    public readonly pathId!: pulumi.Output<string | undefined>;
    public readonly pathName!: pulumi.Output<string | undefined>;
    public readonly productId!: pulumi.Output<string | undefined>;
    public readonly productName!: pulumi.Output<string | undefined>;
    public /*out*/ readonly provisionedProductId!: pulumi.Output<string>;
    public readonly provisionedProductName!: pulumi.Output<string | undefined>;
    public readonly provisioningArtifactId!: pulumi.Output<string | undefined>;
    public readonly provisioningArtifactName!: pulumi.Output<string | undefined>;
    public readonly provisioningParameters!: pulumi.Output<outputs.servicecatalog.CloudFormationProvisionedProductProvisioningParameter[] | undefined>;
    public readonly provisioningPreferences!: pulumi.Output<outputs.servicecatalog.CloudFormationProvisionedProductProvisioningPreferences | undefined>;
    public /*out*/ readonly recordId!: pulumi.Output<string>;
    public readonly tags!: pulumi.Output<outputs.servicecatalog.CloudFormationProvisionedProductTag[] | undefined>;

    /**
     * Create a CloudFormationProvisionedProduct resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: CloudFormationProvisionedProductArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            resourceInputs["acceptLanguage"] = args ? args.acceptLanguage : undefined;
            resourceInputs["notificationArns"] = args ? args.notificationArns : undefined;
            resourceInputs["pathId"] = args ? args.pathId : undefined;
            resourceInputs["pathName"] = args ? args.pathName : undefined;
            resourceInputs["productId"] = args ? args.productId : undefined;
            resourceInputs["productName"] = args ? args.productName : undefined;
            resourceInputs["provisionedProductName"] = args ? args.provisionedProductName : undefined;
            resourceInputs["provisioningArtifactId"] = args ? args.provisioningArtifactId : undefined;
            resourceInputs["provisioningArtifactName"] = args ? args.provisioningArtifactName : undefined;
            resourceInputs["provisioningParameters"] = args ? args.provisioningParameters : undefined;
            resourceInputs["provisioningPreferences"] = args ? args.provisioningPreferences : undefined;
            resourceInputs["tags"] = args ? args.tags : undefined;
            resourceInputs["cloudformationStackArn"] = undefined /*out*/;
            resourceInputs["outputs"] = undefined /*out*/;
            resourceInputs["provisionedProductId"] = undefined /*out*/;
            resourceInputs["recordId"] = undefined /*out*/;
        } else {
            resourceInputs["acceptLanguage"] = undefined /*out*/;
            resourceInputs["cloudformationStackArn"] = undefined /*out*/;
            resourceInputs["notificationArns"] = undefined /*out*/;
            resourceInputs["outputs"] = undefined /*out*/;
            resourceInputs["pathId"] = undefined /*out*/;
            resourceInputs["pathName"] = undefined /*out*/;
            resourceInputs["productId"] = undefined /*out*/;
            resourceInputs["productName"] = undefined /*out*/;
            resourceInputs["provisionedProductId"] = undefined /*out*/;
            resourceInputs["provisionedProductName"] = undefined /*out*/;
            resourceInputs["provisioningArtifactId"] = undefined /*out*/;
            resourceInputs["provisioningArtifactName"] = undefined /*out*/;
            resourceInputs["provisioningParameters"] = undefined /*out*/;
            resourceInputs["provisioningPreferences"] = undefined /*out*/;
            resourceInputs["recordId"] = undefined /*out*/;
            resourceInputs["tags"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const replaceOnChanges = { replaceOnChanges: ["notificationArns[*]", "provisionedProductName"] };
        opts = pulumi.mergeOptions(opts, replaceOnChanges);
        super(CloudFormationProvisionedProduct.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a CloudFormationProvisionedProduct resource.
 */
export interface CloudFormationProvisionedProductArgs {
    acceptLanguage?: pulumi.Input<enums.servicecatalog.CloudFormationProvisionedProductAcceptLanguage>;
    notificationArns?: pulumi.Input<pulumi.Input<string>[]>;
    pathId?: pulumi.Input<string>;
    pathName?: pulumi.Input<string>;
    productId?: pulumi.Input<string>;
    productName?: pulumi.Input<string>;
    provisionedProductName?: pulumi.Input<string>;
    provisioningArtifactId?: pulumi.Input<string>;
    provisioningArtifactName?: pulumi.Input<string>;
    provisioningParameters?: pulumi.Input<pulumi.Input<inputs.servicecatalog.CloudFormationProvisionedProductProvisioningParameterArgs>[]>;
    provisioningPreferences?: pulumi.Input<inputs.servicecatalog.CloudFormationProvisionedProductProvisioningPreferencesArgs>;
    tags?: pulumi.Input<pulumi.Input<inputs.servicecatalog.CloudFormationProvisionedProductTagArgs>[]>;
}
