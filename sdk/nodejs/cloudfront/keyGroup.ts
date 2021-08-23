// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs } from "../types";
import * as utilities from "../utilities";

/**
 * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-keygroup.html
 */
export class KeyGroup extends pulumi.CustomResource {
    /**
     * Get an existing KeyGroup resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): KeyGroup {
        return new KeyGroup(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:cloudfront:KeyGroup';

    /**
     * Returns true if the given object is an instance of KeyGroup.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is KeyGroup {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === KeyGroup.__pulumiType;
    }

    public /*out*/ readonly id!: pulumi.Output<string>;
    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-keygroup.html#cfn-cloudfront-keygroup-keygroupconfig
     */
    public readonly keyGroupConfig!: pulumi.Output<outputs.cloudfront.KeyGroupKeyGroupConfig>;
    public /*out*/ readonly lastModifiedTime!: pulumi.Output<string>;

    /**
     * Create a KeyGroup resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: KeyGroupArgs, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.keyGroupConfig === undefined) && !opts.urn) {
                throw new Error("Missing required property 'keyGroupConfig'");
            }
            inputs["keyGroupConfig"] = args ? args.keyGroupConfig : undefined;
            inputs["id"] = undefined /*out*/;
            inputs["lastModifiedTime"] = undefined /*out*/;
        } else {
            inputs["id"] = undefined /*out*/;
            inputs["keyGroupConfig"] = undefined /*out*/;
            inputs["lastModifiedTime"] = undefined /*out*/;
        }
        if (!opts.version) {
            opts = pulumi.mergeOptions(opts, { version: utilities.getVersion()});
        }
        super(KeyGroup.__pulumiType, name, inputs, opts);
    }
}

/**
 * The set of arguments for constructing a KeyGroup resource.
 */
export interface KeyGroupArgs {
    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-keygroup.html#cfn-cloudfront-keygroup-keygroupconfig
     */
    keyGroupConfig: pulumi.Input<inputs.cloudfront.KeyGroupKeyGroupConfigArgs>;
}
