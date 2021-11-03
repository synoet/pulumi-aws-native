// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs, enums } from "../types";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::MemoryDB::ACL
 */
export class ACL extends pulumi.CustomResource {
    /**
     * Get an existing ACL resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): ACL {
        return new ACL(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:memorydb:ACL';

    /**
     * Returns true if the given object is an instance of ACL.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is ACL {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === ACL.__pulumiType;
    }

    /**
     * The name of the acl.
     */
    public readonly aCLName!: pulumi.Output<string>;
    /**
     * The Amazon Resource Name (ARN) of the acl.
     */
    public /*out*/ readonly arn!: pulumi.Output<string>;
    /**
     * Indicates acl status. Can be "creating", "active", "modifying", "deleting".
     */
    public /*out*/ readonly status!: pulumi.Output<string>;
    /**
     * An array of key-value pairs to apply to this cluster.
     */
    public readonly tags!: pulumi.Output<outputs.memorydb.ACLTag[] | undefined>;
    /**
     * List of users associated to this acl.
     */
    public readonly userNames!: pulumi.Output<string[] | undefined>;

    /**
     * Create a ACL resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: ACLArgs, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            inputs["aCLName"] = args ? args.aCLName : undefined;
            inputs["tags"] = args ? args.tags : undefined;
            inputs["userNames"] = args ? args.userNames : undefined;
            inputs["arn"] = undefined /*out*/;
            inputs["status"] = undefined /*out*/;
        } else {
            inputs["aCLName"] = undefined /*out*/;
            inputs["arn"] = undefined /*out*/;
            inputs["status"] = undefined /*out*/;
            inputs["tags"] = undefined /*out*/;
            inputs["userNames"] = undefined /*out*/;
        }
        if (!opts.version) {
            opts = pulumi.mergeOptions(opts, { version: utilities.getVersion()});
        }
        super(ACL.__pulumiType, name, inputs, opts);
    }
}

/**
 * The set of arguments for constructing a ACL resource.
 */
export interface ACLArgs {
    /**
     * The name of the acl.
     */
    aCLName?: pulumi.Input<string>;
    /**
     * An array of key-value pairs to apply to this cluster.
     */
    tags?: pulumi.Input<pulumi.Input<inputs.memorydb.ACLTagArgs>[]>;
    /**
     * List of users associated to this acl.
     */
    userNames?: pulumi.Input<pulumi.Input<string>[]>;
}
