// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * The AWS::EC2::VerifiedAccessGroup resource creates an AWS EC2 Verified Access Group.
 */
export class VerifiedAccessGroup extends pulumi.CustomResource {
    /**
     * Get an existing VerifiedAccessGroup resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): VerifiedAccessGroup {
        return new VerifiedAccessGroup(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:ec2:VerifiedAccessGroup';

    /**
     * Returns true if the given object is an instance of VerifiedAccessGroup.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is VerifiedAccessGroup {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === VerifiedAccessGroup.__pulumiType;
    }

    /**
     * Time this Verified Access Group was created.
     */
    public /*out*/ readonly creationTime!: pulumi.Output<string>;
    /**
     * A description for the AWS Verified Access group.
     */
    public readonly description!: pulumi.Output<string | undefined>;
    /**
     * Time this Verified Access Group was last updated.
     */
    public /*out*/ readonly lastUpdatedTime!: pulumi.Output<string>;
    /**
     * The AWS account number that owns the group.
     */
    public /*out*/ readonly owner!: pulumi.Output<string>;
    /**
     * The AWS Verified Access policy document.
     */
    public readonly policyDocument!: pulumi.Output<string | undefined>;
    /**
     * The status of the Verified Access policy.
     */
    public readonly policyEnabled!: pulumi.Output<boolean | undefined>;
    /**
     * An array of key-value pairs to apply to this resource.
     */
    public readonly tags!: pulumi.Output<outputs.ec2.VerifiedAccessGroupTag[] | undefined>;
    /**
     * The ARN of the Verified Access group.
     */
    public /*out*/ readonly verifiedAccessGroupArn!: pulumi.Output<string>;
    /**
     * The ID of the AWS Verified Access group.
     */
    public /*out*/ readonly verifiedAccessGroupId!: pulumi.Output<string>;
    /**
     * The ID of the AWS Verified Access instance.
     */
    public readonly verifiedAccessInstanceId!: pulumi.Output<string>;

    /**
     * Create a VerifiedAccessGroup resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: VerifiedAccessGroupArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.verifiedAccessInstanceId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'verifiedAccessInstanceId'");
            }
            resourceInputs["description"] = args ? args.description : undefined;
            resourceInputs["policyDocument"] = args ? args.policyDocument : undefined;
            resourceInputs["policyEnabled"] = args ? args.policyEnabled : undefined;
            resourceInputs["tags"] = args ? args.tags : undefined;
            resourceInputs["verifiedAccessInstanceId"] = args ? args.verifiedAccessInstanceId : undefined;
            resourceInputs["creationTime"] = undefined /*out*/;
            resourceInputs["lastUpdatedTime"] = undefined /*out*/;
            resourceInputs["owner"] = undefined /*out*/;
            resourceInputs["verifiedAccessGroupArn"] = undefined /*out*/;
            resourceInputs["verifiedAccessGroupId"] = undefined /*out*/;
        } else {
            resourceInputs["creationTime"] = undefined /*out*/;
            resourceInputs["description"] = undefined /*out*/;
            resourceInputs["lastUpdatedTime"] = undefined /*out*/;
            resourceInputs["owner"] = undefined /*out*/;
            resourceInputs["policyDocument"] = undefined /*out*/;
            resourceInputs["policyEnabled"] = undefined /*out*/;
            resourceInputs["tags"] = undefined /*out*/;
            resourceInputs["verifiedAccessGroupArn"] = undefined /*out*/;
            resourceInputs["verifiedAccessGroupId"] = undefined /*out*/;
            resourceInputs["verifiedAccessInstanceId"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(VerifiedAccessGroup.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a VerifiedAccessGroup resource.
 */
export interface VerifiedAccessGroupArgs {
    /**
     * A description for the AWS Verified Access group.
     */
    description?: pulumi.Input<string>;
    /**
     * The AWS Verified Access policy document.
     */
    policyDocument?: pulumi.Input<string>;
    /**
     * The status of the Verified Access policy.
     */
    policyEnabled?: pulumi.Input<boolean>;
    /**
     * An array of key-value pairs to apply to this resource.
     */
    tags?: pulumi.Input<pulumi.Input<inputs.ec2.VerifiedAccessGroupTagArgs>[]>;
    /**
     * The ID of the AWS Verified Access instance.
     */
    verifiedAccessInstanceId: pulumi.Input<string>;
}
