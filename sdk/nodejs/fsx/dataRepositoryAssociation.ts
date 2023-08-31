// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::FSx::DataRepositoryAssociation
 */
export class DataRepositoryAssociation extends pulumi.CustomResource {
    /**
     * Get an existing DataRepositoryAssociation resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): DataRepositoryAssociation {
        return new DataRepositoryAssociation(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:fsx:DataRepositoryAssociation';

    /**
     * Returns true if the given object is an instance of DataRepositoryAssociation.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is DataRepositoryAssociation {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === DataRepositoryAssociation.__pulumiType;
    }

    /**
     * The system-generated, unique ID of the data repository association.
     */
    public /*out*/ readonly associationId!: pulumi.Output<string>;
    /**
     * A boolean flag indicating whether an import data repository task to import metadata should run after the data repository association is created. The task runs if this flag is set to true.
     */
    public readonly batchImportMetaDataOnCreate!: pulumi.Output<boolean | undefined>;
    /**
     * The path to the Amazon S3 data repository that will be linked to the file system. The path can be an S3 bucket or prefix in the format s3://myBucket/myPrefix/ . This path specifies where in the S3 data repository files will be imported from or exported to.
     */
    public readonly dataRepositoryPath!: pulumi.Output<string>;
    /**
     * The globally unique ID of the file system, assigned by Amazon FSx.
     */
    public readonly fileSystemId!: pulumi.Output<string>;
    /**
     * This path specifies where in your file system files will be exported from or imported to. This file system directory can be linked to only one Amazon S3 bucket, and no other S3 bucket can be linked to the directory.
     */
    public readonly fileSystemPath!: pulumi.Output<string>;
    /**
     * For files imported from a data repository, this value determines the stripe count and maximum amount of data per file (in MiB) stored on a single physical disk. The maximum number of disks that a single file can be striped across is limited by the total number of disks that make up the file system.
     */
    public readonly importedFileChunkSize!: pulumi.Output<number | undefined>;
    /**
     * The Amazon Resource Name (ARN) for a given resource. ARNs uniquely identify Amazon Web Services resources. We require an ARN when you need to specify a resource unambiguously across all of Amazon Web Services. For more information, see Amazon Resource Names (ARNs) in the Amazon Web Services General Reference.
     */
    public /*out*/ readonly resourceArn!: pulumi.Output<string>;
    /**
     * The configuration for an Amazon S3 data repository linked to an Amazon FSx Lustre file system with a data repository association. The configuration defines which file events (new, changed, or deleted files or directories) are automatically imported from the linked data repository to the file system or automatically exported from the file system to the data repository.
     */
    public readonly s3!: pulumi.Output<outputs.fsx.DataRepositoryAssociationS3 | undefined>;
    /**
     * A list of Tag values, with a maximum of 50 elements.
     */
    public readonly tags!: pulumi.Output<outputs.fsx.DataRepositoryAssociationTag[] | undefined>;

    /**
     * Create a DataRepositoryAssociation resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: DataRepositoryAssociationArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.dataRepositoryPath === undefined) && !opts.urn) {
                throw new Error("Missing required property 'dataRepositoryPath'");
            }
            if ((!args || args.fileSystemId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'fileSystemId'");
            }
            if ((!args || args.fileSystemPath === undefined) && !opts.urn) {
                throw new Error("Missing required property 'fileSystemPath'");
            }
            resourceInputs["batchImportMetaDataOnCreate"] = args ? args.batchImportMetaDataOnCreate : undefined;
            resourceInputs["dataRepositoryPath"] = args ? args.dataRepositoryPath : undefined;
            resourceInputs["fileSystemId"] = args ? args.fileSystemId : undefined;
            resourceInputs["fileSystemPath"] = args ? args.fileSystemPath : undefined;
            resourceInputs["importedFileChunkSize"] = args ? args.importedFileChunkSize : undefined;
            resourceInputs["s3"] = args ? args.s3 : undefined;
            resourceInputs["tags"] = args ? args.tags : undefined;
            resourceInputs["associationId"] = undefined /*out*/;
            resourceInputs["resourceArn"] = undefined /*out*/;
        } else {
            resourceInputs["associationId"] = undefined /*out*/;
            resourceInputs["batchImportMetaDataOnCreate"] = undefined /*out*/;
            resourceInputs["dataRepositoryPath"] = undefined /*out*/;
            resourceInputs["fileSystemId"] = undefined /*out*/;
            resourceInputs["fileSystemPath"] = undefined /*out*/;
            resourceInputs["importedFileChunkSize"] = undefined /*out*/;
            resourceInputs["resourceArn"] = undefined /*out*/;
            resourceInputs["s3"] = undefined /*out*/;
            resourceInputs["tags"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const replaceOnChanges = { replaceOnChanges: ["batchImportMetaDataOnCreate", "dataRepositoryPath", "fileSystemId", "fileSystemPath"] };
        opts = pulumi.mergeOptions(opts, replaceOnChanges);
        super(DataRepositoryAssociation.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a DataRepositoryAssociation resource.
 */
export interface DataRepositoryAssociationArgs {
    /**
     * A boolean flag indicating whether an import data repository task to import metadata should run after the data repository association is created. The task runs if this flag is set to true.
     */
    batchImportMetaDataOnCreate?: pulumi.Input<boolean>;
    /**
     * The path to the Amazon S3 data repository that will be linked to the file system. The path can be an S3 bucket or prefix in the format s3://myBucket/myPrefix/ . This path specifies where in the S3 data repository files will be imported from or exported to.
     */
    dataRepositoryPath: pulumi.Input<string>;
    /**
     * The globally unique ID of the file system, assigned by Amazon FSx.
     */
    fileSystemId: pulumi.Input<string>;
    /**
     * This path specifies where in your file system files will be exported from or imported to. This file system directory can be linked to only one Amazon S3 bucket, and no other S3 bucket can be linked to the directory.
     */
    fileSystemPath: pulumi.Input<string>;
    /**
     * For files imported from a data repository, this value determines the stripe count and maximum amount of data per file (in MiB) stored on a single physical disk. The maximum number of disks that a single file can be striped across is limited by the total number of disks that make up the file system.
     */
    importedFileChunkSize?: pulumi.Input<number>;
    /**
     * The configuration for an Amazon S3 data repository linked to an Amazon FSx Lustre file system with a data repository association. The configuration defines which file events (new, changed, or deleted files or directories) are automatically imported from the linked data repository to the file system or automatically exported from the file system to the data repository.
     */
    s3?: pulumi.Input<inputs.fsx.DataRepositoryAssociationS3Args>;
    /**
     * A list of Tag values, with a maximum of 50 elements.
     */
    tags?: pulumi.Input<pulumi.Input<inputs.fsx.DataRepositoryAssociationTagArgs>[]>;
}
