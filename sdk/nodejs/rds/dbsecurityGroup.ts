// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::RDS::DBSecurityGroup
 *
 * @deprecated DBSecurityGroup is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.
 */
export class DBSecurityGroup extends pulumi.CustomResource {
    /**
     * Get an existing DBSecurityGroup resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): DBSecurityGroup {
        pulumi.log.warn("DBSecurityGroup is deprecated: DBSecurityGroup is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.")
        return new DBSecurityGroup(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:rds:DBSecurityGroup';

    /**
     * Returns true if the given object is an instance of DBSecurityGroup.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is DBSecurityGroup {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === DBSecurityGroup.__pulumiType;
    }

    public readonly dbSecurityGroupIngress!: pulumi.Output<outputs.rds.DBSecurityGroupIngress[]>;
    public readonly ec2VpcId!: pulumi.Output<string | undefined>;
    public readonly groupDescription!: pulumi.Output<string>;
    public readonly tags!: pulumi.Output<outputs.rds.DBSecurityGroupTag[] | undefined>;

    /**
     * Create a DBSecurityGroup resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    /** @deprecated DBSecurityGroup is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible. */
    constructor(name: string, args: DBSecurityGroupArgs, opts?: pulumi.CustomResourceOptions) {
        pulumi.log.warn("DBSecurityGroup is deprecated: DBSecurityGroup is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.")
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.dbSecurityGroupIngress === undefined) && !opts.urn) {
                throw new Error("Missing required property 'dbSecurityGroupIngress'");
            }
            if ((!args || args.groupDescription === undefined) && !opts.urn) {
                throw new Error("Missing required property 'groupDescription'");
            }
            resourceInputs["dbSecurityGroupIngress"] = args ? args.dbSecurityGroupIngress : undefined;
            resourceInputs["ec2VpcId"] = args ? args.ec2VpcId : undefined;
            resourceInputs["groupDescription"] = args ? args.groupDescription : undefined;
            resourceInputs["tags"] = args ? args.tags : undefined;
        } else {
            resourceInputs["dbSecurityGroupIngress"] = undefined /*out*/;
            resourceInputs["ec2VpcId"] = undefined /*out*/;
            resourceInputs["groupDescription"] = undefined /*out*/;
            resourceInputs["tags"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(DBSecurityGroup.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a DBSecurityGroup resource.
 */
export interface DBSecurityGroupArgs {
    dbSecurityGroupIngress: pulumi.Input<pulumi.Input<inputs.rds.DBSecurityGroupIngressArgs>[]>;
    ec2VpcId?: pulumi.Input<string>;
    groupDescription: pulumi.Input<string>;
    tags?: pulumi.Input<pulumi.Input<inputs.rds.DBSecurityGroupTagArgs>[]>;
}
