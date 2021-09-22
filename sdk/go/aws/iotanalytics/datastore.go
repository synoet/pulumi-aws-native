// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package iotanalytics

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource Type definition for AWS::IoTAnalytics::Datastore
//
// Deprecated: Datastore is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible.
type Datastore struct {
	pulumi.CustomResourceState

	DatastoreName           pulumi.StringPtrOutput                    `pulumi:"datastoreName"`
	DatastorePartitions     DatastoreDatastorePartitionsPtrOutput     `pulumi:"datastorePartitions"`
	DatastoreStorage        DatastoreDatastoreStoragePtrOutput        `pulumi:"datastoreStorage"`
	FileFormatConfiguration DatastoreFileFormatConfigurationPtrOutput `pulumi:"fileFormatConfiguration"`
	RetentionPeriod         DatastoreRetentionPeriodPtrOutput         `pulumi:"retentionPeriod"`
	Tags                    DatastoreTagArrayOutput                   `pulumi:"tags"`
}

// NewDatastore registers a new resource with the given unique name, arguments, and options.
func NewDatastore(ctx *pulumi.Context,
	name string, args *DatastoreArgs, opts ...pulumi.ResourceOption) (*Datastore, error) {
	if args == nil {
		args = &DatastoreArgs{}
	}

	var resource Datastore
	err := ctx.RegisterResource("aws-native:iotanalytics:Datastore", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetDatastore gets an existing Datastore resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetDatastore(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *DatastoreState, opts ...pulumi.ResourceOption) (*Datastore, error) {
	var resource Datastore
	err := ctx.ReadResource("aws-native:iotanalytics:Datastore", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Datastore resources.
type datastoreState struct {
}

type DatastoreState struct {
}

func (DatastoreState) ElementType() reflect.Type {
	return reflect.TypeOf((*datastoreState)(nil)).Elem()
}

type datastoreArgs struct {
	DatastoreName           *string                           `pulumi:"datastoreName"`
	DatastorePartitions     *DatastoreDatastorePartitions     `pulumi:"datastorePartitions"`
	DatastoreStorage        *DatastoreDatastoreStorage        `pulumi:"datastoreStorage"`
	FileFormatConfiguration *DatastoreFileFormatConfiguration `pulumi:"fileFormatConfiguration"`
	RetentionPeriod         *DatastoreRetentionPeriod         `pulumi:"retentionPeriod"`
	Tags                    []DatastoreTag                    `pulumi:"tags"`
}

// The set of arguments for constructing a Datastore resource.
type DatastoreArgs struct {
	DatastoreName           pulumi.StringPtrInput
	DatastorePartitions     DatastoreDatastorePartitionsPtrInput
	DatastoreStorage        DatastoreDatastoreStoragePtrInput
	FileFormatConfiguration DatastoreFileFormatConfigurationPtrInput
	RetentionPeriod         DatastoreRetentionPeriodPtrInput
	Tags                    DatastoreTagArrayInput
}

func (DatastoreArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*datastoreArgs)(nil)).Elem()
}

type DatastoreInput interface {
	pulumi.Input

	ToDatastoreOutput() DatastoreOutput
	ToDatastoreOutputWithContext(ctx context.Context) DatastoreOutput
}

func (*Datastore) ElementType() reflect.Type {
	return reflect.TypeOf((*Datastore)(nil))
}

func (i *Datastore) ToDatastoreOutput() DatastoreOutput {
	return i.ToDatastoreOutputWithContext(context.Background())
}

func (i *Datastore) ToDatastoreOutputWithContext(ctx context.Context) DatastoreOutput {
	return pulumi.ToOutputWithContext(ctx, i).(DatastoreOutput)
}

type DatastoreOutput struct{ *pulumi.OutputState }

func (DatastoreOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*Datastore)(nil))
}

func (o DatastoreOutput) ToDatastoreOutput() DatastoreOutput {
	return o
}

func (o DatastoreOutput) ToDatastoreOutputWithContext(ctx context.Context) DatastoreOutput {
	return o
}

func init() {
	pulumi.RegisterOutputType(DatastoreOutput{})
}
