// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * The AWS::RDS::CustomDBEngineVersion resource creates an Amazon RDS custom DB engine version.
 */
export class CustomDbEngineVersion extends pulumi.CustomResource {
    /**
     * Get an existing CustomDbEngineVersion resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): CustomDbEngineVersion {
        return new CustomDbEngineVersion(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:rds:CustomDbEngineVersion';

    /**
     * Returns true if the given object is an instance of CustomDbEngineVersion.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is CustomDbEngineVersion {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === CustomDbEngineVersion.__pulumiType;
    }

    /**
     * The name of an Amazon S3 bucket that contains database installation files for your CEV. For example, a valid bucket name is `my-custom-installation-files`.
     */
    public readonly databaseInstallationFilesS3BucketName!: pulumi.Output<string>;
    /**
     * The Amazon S3 directory that contains the database installation files for your CEV. For example, a valid bucket name is `123456789012/cev1`. If this setting isn't specified, no prefix is assumed.
     */
    public readonly databaseInstallationFilesS3Prefix!: pulumi.Output<string | undefined>;
    /**
     * The ARN of the custom engine version.
     */
    public /*out*/ readonly dbEngineVersionArn!: pulumi.Output<string>;
    /**
     * An optional description of your CEV.
     */
    public readonly description!: pulumi.Output<string | undefined>;
    /**
     * The database engine to use for your custom engine version (CEV). The only supported value is `custom-oracle-ee`.
     */
    public readonly engine!: pulumi.Output<string>;
    /**
     * The name of your CEV. The name format is 19.customized_string . For example, a valid name is 19.my_cev1. This setting is required for RDS Custom for Oracle, but optional for Amazon RDS. The combination of Engine and EngineVersion is unique per customer per Region.
     */
    public readonly engineVersion!: pulumi.Output<string>;
    /**
     * The AWS KMS key identifier for an encrypted CEV. A symmetric KMS key is required for RDS Custom, but optional for Amazon RDS.
     */
    public readonly kmsKeyId!: pulumi.Output<string | undefined>;
    /**
     * The CEV manifest, which is a JSON document that describes the installation .zip files stored in Amazon S3. Specify the name/value pairs in a file or a quoted string. RDS Custom applies the patches in the order in which they are listed.
     */
    public readonly manifest!: pulumi.Output<string | undefined>;
    /**
     * The availability status to be assigned to the CEV.
     */
    public readonly status!: pulumi.Output<enums.rds.CustomDbEngineVersionStatus | undefined>;
    /**
     * An array of key-value pairs to apply to this resource.
     */
    public readonly tags!: pulumi.Output<outputs.rds.CustomDbEngineVersionTag[] | undefined>;

    /**
     * Create a CustomDbEngineVersion resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: CustomDbEngineVersionArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.databaseInstallationFilesS3BucketName === undefined) && !opts.urn) {
                throw new Error("Missing required property 'databaseInstallationFilesS3BucketName'");
            }
            if ((!args || args.engine === undefined) && !opts.urn) {
                throw new Error("Missing required property 'engine'");
            }
            if ((!args || args.engineVersion === undefined) && !opts.urn) {
                throw new Error("Missing required property 'engineVersion'");
            }
            resourceInputs["databaseInstallationFilesS3BucketName"] = args ? args.databaseInstallationFilesS3BucketName : undefined;
            resourceInputs["databaseInstallationFilesS3Prefix"] = args ? args.databaseInstallationFilesS3Prefix : undefined;
            resourceInputs["description"] = args ? args.description : undefined;
            resourceInputs["engine"] = args ? args.engine : undefined;
            resourceInputs["engineVersion"] = args ? args.engineVersion : undefined;
            resourceInputs["kmsKeyId"] = args ? args.kmsKeyId : undefined;
            resourceInputs["manifest"] = args ? args.manifest : undefined;
            resourceInputs["status"] = args ? args.status : undefined;
            resourceInputs["tags"] = args ? args.tags : undefined;
            resourceInputs["dbEngineVersionArn"] = undefined /*out*/;
        } else {
            resourceInputs["databaseInstallationFilesS3BucketName"] = undefined /*out*/;
            resourceInputs["databaseInstallationFilesS3Prefix"] = undefined /*out*/;
            resourceInputs["dbEngineVersionArn"] = undefined /*out*/;
            resourceInputs["description"] = undefined /*out*/;
            resourceInputs["engine"] = undefined /*out*/;
            resourceInputs["engineVersion"] = undefined /*out*/;
            resourceInputs["kmsKeyId"] = undefined /*out*/;
            resourceInputs["manifest"] = undefined /*out*/;
            resourceInputs["status"] = undefined /*out*/;
            resourceInputs["tags"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const replaceOnChanges = { replaceOnChanges: ["databaseInstallationFilesS3BucketName", "databaseInstallationFilesS3Prefix", "engine", "engineVersion", "kmsKeyId", "manifest"] };
        opts = pulumi.mergeOptions(opts, replaceOnChanges);
        super(CustomDbEngineVersion.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a CustomDbEngineVersion resource.
 */
export interface CustomDbEngineVersionArgs {
    /**
     * The name of an Amazon S3 bucket that contains database installation files for your CEV. For example, a valid bucket name is `my-custom-installation-files`.
     */
    databaseInstallationFilesS3BucketName: pulumi.Input<string>;
    /**
     * The Amazon S3 directory that contains the database installation files for your CEV. For example, a valid bucket name is `123456789012/cev1`. If this setting isn't specified, no prefix is assumed.
     */
    databaseInstallationFilesS3Prefix?: pulumi.Input<string>;
    /**
     * An optional description of your CEV.
     */
    description?: pulumi.Input<string>;
    /**
     * The database engine to use for your custom engine version (CEV). The only supported value is `custom-oracle-ee`.
     */
    engine: pulumi.Input<string>;
    /**
     * The name of your CEV. The name format is 19.customized_string . For example, a valid name is 19.my_cev1. This setting is required for RDS Custom for Oracle, but optional for Amazon RDS. The combination of Engine and EngineVersion is unique per customer per Region.
     */
    engineVersion: pulumi.Input<string>;
    /**
     * The AWS KMS key identifier for an encrypted CEV. A symmetric KMS key is required for RDS Custom, but optional for Amazon RDS.
     */
    kmsKeyId?: pulumi.Input<string>;
    /**
     * The CEV manifest, which is a JSON document that describes the installation .zip files stored in Amazon S3. Specify the name/value pairs in a file or a quoted string. RDS Custom applies the patches in the order in which they are listed.
     */
    manifest?: pulumi.Input<string>;
    /**
     * The availability status to be assigned to the CEV.
     */
    status?: pulumi.Input<enums.rds.CustomDbEngineVersionStatus>;
    /**
     * An array of key-value pairs to apply to this resource.
     */
    tags?: pulumi.Input<pulumi.Input<inputs.rds.CustomDbEngineVersionTagArgs>[]>;
}
