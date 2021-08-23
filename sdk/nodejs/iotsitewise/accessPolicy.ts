// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs } from "../types";
import * as utilities from "../utilities";

/**
 * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-accesspolicy.html
 */
export class AccessPolicy extends pulumi.CustomResource {
    /**
     * Get an existing AccessPolicy resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): AccessPolicy {
        return new AccessPolicy(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:iotsitewise:AccessPolicy';

    /**
     * Returns true if the given object is an instance of AccessPolicy.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is AccessPolicy {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === AccessPolicy.__pulumiType;
    }

    public /*out*/ readonly accessPolicyArn!: pulumi.Output<string>;
    public /*out*/ readonly accessPolicyId!: pulumi.Output<string>;
    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-accesspolicy.html#cfn-iotsitewise-accesspolicy-accesspolicyidentity
     */
    public readonly accessPolicyIdentity!: pulumi.Output<outputs.iotsitewise.AccessPolicyAccessPolicyIdentity>;
    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-accesspolicy.html#cfn-iotsitewise-accesspolicy-accesspolicypermission
     */
    public readonly accessPolicyPermission!: pulumi.Output<string>;
    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-accesspolicy.html#cfn-iotsitewise-accesspolicy-accesspolicyresource
     */
    public readonly accessPolicyResource!: pulumi.Output<outputs.iotsitewise.AccessPolicyAccessPolicyResource>;

    /**
     * Create a AccessPolicy resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: AccessPolicyArgs, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.accessPolicyIdentity === undefined) && !opts.urn) {
                throw new Error("Missing required property 'accessPolicyIdentity'");
            }
            if ((!args || args.accessPolicyPermission === undefined) && !opts.urn) {
                throw new Error("Missing required property 'accessPolicyPermission'");
            }
            if ((!args || args.accessPolicyResource === undefined) && !opts.urn) {
                throw new Error("Missing required property 'accessPolicyResource'");
            }
            inputs["accessPolicyIdentity"] = args ? args.accessPolicyIdentity : undefined;
            inputs["accessPolicyPermission"] = args ? args.accessPolicyPermission : undefined;
            inputs["accessPolicyResource"] = args ? args.accessPolicyResource : undefined;
            inputs["accessPolicyArn"] = undefined /*out*/;
            inputs["accessPolicyId"] = undefined /*out*/;
        } else {
            inputs["accessPolicyArn"] = undefined /*out*/;
            inputs["accessPolicyId"] = undefined /*out*/;
            inputs["accessPolicyIdentity"] = undefined /*out*/;
            inputs["accessPolicyPermission"] = undefined /*out*/;
            inputs["accessPolicyResource"] = undefined /*out*/;
        }
        if (!opts.version) {
            opts = pulumi.mergeOptions(opts, { version: utilities.getVersion()});
        }
        super(AccessPolicy.__pulumiType, name, inputs, opts);
    }
}

/**
 * The set of arguments for constructing a AccessPolicy resource.
 */
export interface AccessPolicyArgs {
    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-accesspolicy.html#cfn-iotsitewise-accesspolicy-accesspolicyidentity
     */
    accessPolicyIdentity: pulumi.Input<inputs.iotsitewise.AccessPolicyAccessPolicyIdentityArgs>;
    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-accesspolicy.html#cfn-iotsitewise-accesspolicy-accesspolicypermission
     */
    accessPolicyPermission: pulumi.Input<string>;
    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-accesspolicy.html#cfn-iotsitewise-accesspolicy-accesspolicyresource
     */
    accessPolicyResource: pulumi.Input<inputs.iotsitewise.AccessPolicyAccessPolicyResourceArgs>;
}
