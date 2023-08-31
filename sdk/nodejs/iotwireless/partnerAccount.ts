// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Create and manage partner account
 *
 * @deprecated PartnerAccount is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.
 */
export class PartnerAccount extends pulumi.CustomResource {
    /**
     * Get an existing PartnerAccount resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): PartnerAccount {
        pulumi.log.warn("PartnerAccount is deprecated: PartnerAccount is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.")
        return new PartnerAccount(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:iotwireless:PartnerAccount';

    /**
     * Returns true if the given object is an instance of PartnerAccount.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is PartnerAccount {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === PartnerAccount.__pulumiType;
    }

    /**
     * Whether the partner account is linked to the AWS account.
     */
    public readonly accountLinked!: pulumi.Output<boolean | undefined>;
    /**
     * PartnerAccount arn. Returned after successful create.
     */
    public /*out*/ readonly arn!: pulumi.Output<string>;
    /**
     * The fingerprint of the Sidewalk application server private key.
     */
    public /*out*/ readonly fingerprint!: pulumi.Output<string>;
    /**
     * The partner account ID to disassociate from the AWS account
     */
    public readonly partnerAccountId!: pulumi.Output<string | undefined>;
    /**
     * The partner type
     */
    public readonly partnerType!: pulumi.Output<enums.iotwireless.PartnerAccountPartnerType | undefined>;
    /**
     * The Sidewalk account credentials.
     */
    public readonly sidewalk!: pulumi.Output<outputs.iotwireless.PartnerAccountSidewalkAccountInfo | undefined>;
    /**
     * The Sidewalk account credentials.
     */
    public readonly sidewalkResponse!: pulumi.Output<outputs.iotwireless.PartnerAccountSidewalkAccountInfoWithFingerprint | undefined>;
    /**
     * The Sidewalk account credentials.
     */
    public readonly sidewalkUpdate!: pulumi.Output<outputs.iotwireless.PartnerAccountSidewalkUpdateAccount | undefined>;
    /**
     * A list of key-value pairs that contain metadata for the destination.
     */
    public readonly tags!: pulumi.Output<outputs.iotwireless.PartnerAccountTag[] | undefined>;

    /**
     * Create a PartnerAccount resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    /** @deprecated PartnerAccount is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible. */
    constructor(name: string, args?: PartnerAccountArgs, opts?: pulumi.CustomResourceOptions) {
        pulumi.log.warn("PartnerAccount is deprecated: PartnerAccount is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.")
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            resourceInputs["accountLinked"] = args ? args.accountLinked : undefined;
            resourceInputs["partnerAccountId"] = args ? args.partnerAccountId : undefined;
            resourceInputs["partnerType"] = args ? args.partnerType : undefined;
            resourceInputs["sidewalk"] = args ? args.sidewalk : undefined;
            resourceInputs["sidewalkResponse"] = args ? args.sidewalkResponse : undefined;
            resourceInputs["sidewalkUpdate"] = args ? args.sidewalkUpdate : undefined;
            resourceInputs["tags"] = args ? args.tags : undefined;
            resourceInputs["arn"] = undefined /*out*/;
            resourceInputs["fingerprint"] = undefined /*out*/;
        } else {
            resourceInputs["accountLinked"] = undefined /*out*/;
            resourceInputs["arn"] = undefined /*out*/;
            resourceInputs["fingerprint"] = undefined /*out*/;
            resourceInputs["partnerAccountId"] = undefined /*out*/;
            resourceInputs["partnerType"] = undefined /*out*/;
            resourceInputs["sidewalk"] = undefined /*out*/;
            resourceInputs["sidewalkResponse"] = undefined /*out*/;
            resourceInputs["sidewalkUpdate"] = undefined /*out*/;
            resourceInputs["tags"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const replaceOnChanges = { replaceOnChanges: ["partnerAccountId"] };
        opts = pulumi.mergeOptions(opts, replaceOnChanges);
        super(PartnerAccount.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a PartnerAccount resource.
 */
export interface PartnerAccountArgs {
    /**
     * Whether the partner account is linked to the AWS account.
     */
    accountLinked?: pulumi.Input<boolean>;
    /**
     * The partner account ID to disassociate from the AWS account
     */
    partnerAccountId?: pulumi.Input<string>;
    /**
     * The partner type
     */
    partnerType?: pulumi.Input<enums.iotwireless.PartnerAccountPartnerType>;
    /**
     * The Sidewalk account credentials.
     */
    sidewalk?: pulumi.Input<inputs.iotwireless.PartnerAccountSidewalkAccountInfoArgs>;
    /**
     * The Sidewalk account credentials.
     */
    sidewalkResponse?: pulumi.Input<inputs.iotwireless.PartnerAccountSidewalkAccountInfoWithFingerprintArgs>;
    /**
     * The Sidewalk account credentials.
     */
    sidewalkUpdate?: pulumi.Input<inputs.iotwireless.PartnerAccountSidewalkUpdateAccountArgs>;
    /**
     * A list of key-value pairs that contain metadata for the destination.
     */
    tags?: pulumi.Input<pulumi.Input<inputs.iotwireless.PartnerAccountTagArgs>[]>;
}
