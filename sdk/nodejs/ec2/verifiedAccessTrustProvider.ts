// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * The AWS::EC2::VerifiedAccessTrustProvider type describes a verified access trust provider
 */
export class VerifiedAccessTrustProvider extends pulumi.CustomResource {
    /**
     * Get an existing VerifiedAccessTrustProvider resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): VerifiedAccessTrustProvider {
        return new VerifiedAccessTrustProvider(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:ec2:VerifiedAccessTrustProvider';

    /**
     * Returns true if the given object is an instance of VerifiedAccessTrustProvider.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is VerifiedAccessTrustProvider {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === VerifiedAccessTrustProvider.__pulumiType;
    }

    /**
     * The creation time.
     */
    public /*out*/ readonly creationTime!: pulumi.Output<string>;
    /**
     * A description for the Amazon Web Services Verified Access trust provider.
     */
    public readonly description!: pulumi.Output<string | undefined>;
    public readonly deviceOptions!: pulumi.Output<outputs.ec2.VerifiedAccessTrustProviderDeviceOptions | undefined>;
    /**
     * The type of device-based trust provider. Possible values: jamf|crowdstrike
     */
    public readonly deviceTrustProviderType!: pulumi.Output<string | undefined>;
    /**
     * The last updated time.
     */
    public /*out*/ readonly lastUpdatedTime!: pulumi.Output<string>;
    public readonly oidcOptions!: pulumi.Output<outputs.ec2.VerifiedAccessTrustProviderOidcOptions | undefined>;
    /**
     * The identifier to be used when working with policy rules.
     */
    public readonly policyReferenceName!: pulumi.Output<string>;
    /**
     * An array of key-value pairs to apply to this resource.
     */
    public readonly tags!: pulumi.Output<outputs.ec2.VerifiedAccessTrustProviderTag[] | undefined>;
    /**
     * Type of trust provider. Possible values: user|device
     */
    public readonly trustProviderType!: pulumi.Output<string>;
    /**
     * The type of device-based trust provider. Possible values: oidc|iam-identity-center
     */
    public readonly userTrustProviderType!: pulumi.Output<string | undefined>;
    /**
     * The ID of the Amazon Web Services Verified Access trust provider.
     */
    public /*out*/ readonly verifiedAccessTrustProviderId!: pulumi.Output<string>;

    /**
     * Create a VerifiedAccessTrustProvider resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: VerifiedAccessTrustProviderArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.policyReferenceName === undefined) && !opts.urn) {
                throw new Error("Missing required property 'policyReferenceName'");
            }
            if ((!args || args.trustProviderType === undefined) && !opts.urn) {
                throw new Error("Missing required property 'trustProviderType'");
            }
            resourceInputs["description"] = args ? args.description : undefined;
            resourceInputs["deviceOptions"] = args ? args.deviceOptions : undefined;
            resourceInputs["deviceTrustProviderType"] = args ? args.deviceTrustProviderType : undefined;
            resourceInputs["oidcOptions"] = args ? args.oidcOptions : undefined;
            resourceInputs["policyReferenceName"] = args ? args.policyReferenceName : undefined;
            resourceInputs["tags"] = args ? args.tags : undefined;
            resourceInputs["trustProviderType"] = args ? args.trustProviderType : undefined;
            resourceInputs["userTrustProviderType"] = args ? args.userTrustProviderType : undefined;
            resourceInputs["creationTime"] = undefined /*out*/;
            resourceInputs["lastUpdatedTime"] = undefined /*out*/;
            resourceInputs["verifiedAccessTrustProviderId"] = undefined /*out*/;
        } else {
            resourceInputs["creationTime"] = undefined /*out*/;
            resourceInputs["description"] = undefined /*out*/;
            resourceInputs["deviceOptions"] = undefined /*out*/;
            resourceInputs["deviceTrustProviderType"] = undefined /*out*/;
            resourceInputs["lastUpdatedTime"] = undefined /*out*/;
            resourceInputs["oidcOptions"] = undefined /*out*/;
            resourceInputs["policyReferenceName"] = undefined /*out*/;
            resourceInputs["tags"] = undefined /*out*/;
            resourceInputs["trustProviderType"] = undefined /*out*/;
            resourceInputs["userTrustProviderType"] = undefined /*out*/;
            resourceInputs["verifiedAccessTrustProviderId"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const replaceOnChanges = { replaceOnChanges: ["deviceOptions", "deviceTrustProviderType", "policyReferenceName", "trustProviderType", "userTrustProviderType"] };
        opts = pulumi.mergeOptions(opts, replaceOnChanges);
        super(VerifiedAccessTrustProvider.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a VerifiedAccessTrustProvider resource.
 */
export interface VerifiedAccessTrustProviderArgs {
    /**
     * A description for the Amazon Web Services Verified Access trust provider.
     */
    description?: pulumi.Input<string>;
    deviceOptions?: pulumi.Input<inputs.ec2.VerifiedAccessTrustProviderDeviceOptionsArgs>;
    /**
     * The type of device-based trust provider. Possible values: jamf|crowdstrike
     */
    deviceTrustProviderType?: pulumi.Input<string>;
    oidcOptions?: pulumi.Input<inputs.ec2.VerifiedAccessTrustProviderOidcOptionsArgs>;
    /**
     * The identifier to be used when working with policy rules.
     */
    policyReferenceName: pulumi.Input<string>;
    /**
     * An array of key-value pairs to apply to this resource.
     */
    tags?: pulumi.Input<pulumi.Input<inputs.ec2.VerifiedAccessTrustProviderTagArgs>[]>;
    /**
     * Type of trust provider. Possible values: user|device
     */
    trustProviderType: pulumi.Input<string>;
    /**
     * The type of device-based trust provider. Possible values: oidc|iam-identity-center
     */
    userTrustProviderType?: pulumi.Input<string>;
}
